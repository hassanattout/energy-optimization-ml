from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "data.csv"


def generate_dataset(seed: int = 42, days: int = 120) -> pd.DataFrame:
    """Generate a reproducible synthetic building-energy dataset."""
    rng = np.random.default_rng(seed)
    hours = 24 * days
    time = pd.date_range("2024-01-01", periods=hours, freq="h")

    df = pd.DataFrame({"timestamp": time})
    df["hour"] = df["timestamp"].dt.hour
    df["temp"] = (
        10
        + 10 * np.sin(2 * np.pi * df["hour"] / 24)
        + rng.normal(size=hours)
    )
    df["occupancy"] = np.where(
        (df["hour"] >= 8) & (df["hour"] <= 18), 1.0, 0.3
    )
    df["energy"] = (
        50
        + 40 * df["occupancy"]
        + 3 * np.abs(df["temp"] - 18)
        + rng.normal(scale=3, size=hours)
    )
    return df


def main() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    generate_dataset().to_csv(DATA_PATH, index=False)
    print(f"Dataset created: {DATA_PATH}")


if __name__ == "__main__":
    main()
