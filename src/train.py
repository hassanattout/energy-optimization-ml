from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "data.csv"
MODEL_PATH = ROOT / "models" / "model.pkl"
OUTPUT_PATH = ROOT / "outputs" / "model.png"
FEATURES = ["hour", "temp", "occupancy"]


def train_model(data_path: Path = DATA_PATH) -> float:
    """Train with a chronological holdout and return holdout RMSE."""
    df = pd.read_csv(data_path).sort_values("timestamp")
    split_index = int(len(df) * 0.8)
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(train_df[FEATURES], train_df["energy"])
    predictions = model.predict(test_df[FEATURES])
    rmse = float(
        np.sqrt(mean_squared_error(test_df["energy"], predictions))
    )

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    plt.figure(figsize=(7, 5))
    plt.scatter(test_df["energy"], predictions, alpha=0.3)
    maximum = max(test_df["energy"].max(), predictions.max())
    plt.plot([0, maximum], [0, maximum], "--")
    plt.title("Chronological holdout: predicted vs actual")
    plt.xlabel("Actual energy")
    plt.ylabel("Predicted energy")
    plt.text(
        test_df["energy"].min(),
        test_df["energy"].max() * 0.9,
        f"RMSE: {rmse:.2f}",
    )
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=160)
    plt.close()
    return rmse


def main() -> None:
    rmse = train_model()
    print(f"Chronological holdout RMSE: {rmse:.2f}")


if __name__ == "__main__":
    main()
