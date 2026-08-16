from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "data.csv"
OUTPUT_PATH = ROOT / "outputs" / "optimization.png"


def apply_peak_shaving(
    df: pd.DataFrame,
    peak_quantile: float = 0.85,
    off_peak_quantile: float = 0.30,
    peak_reduction_fraction: float = 0.15,
) -> tuple[pd.DataFrame, dict[str, float]]:
    """Apply an energy-conserving load-shifting heuristic."""
    result = df.copy()
    peak_threshold = result["energy"].quantile(peak_quantile)
    off_peak_threshold = result["energy"].quantile(off_peak_quantile)

    result["optimized"] = result["energy"].copy()
    peak_mask = result["energy"] > peak_threshold
    result.loc[peak_mask, "optimized"] *= 1 - peak_reduction_fraction

    shifted_energy = float(
        (result["energy"] - result["optimized"]).sum()
    )
    off_peak_mask = result["energy"] < off_peak_threshold
    if not off_peak_mask.any():
        raise ValueError("No off-peak periods were found.")

    result.loc[off_peak_mask, "optimized"] += (
        shifted_energy / int(off_peak_mask.sum())
    )

    peak_before = float(result["energy"].max())
    peak_after = float(result["optimized"].max())
    metrics = {
        "peak_before": peak_before,
        "peak_after": peak_after,
        "peak_reduction_percent": (
            (peak_before - peak_after) / peak_before * 100
        ),
        "energy_balance_error": float(
            result["optimized"].sum() - result["energy"].sum()
        ),
        "peak_threshold": float(peak_threshold),
    }
    return result, metrics


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    optimized, metrics = apply_peak_shaving(df)
    sample = optimized.iloc[:200]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    plt.plot(sample["energy"], label="Original")
    plt.plot(sample["optimized"], label="Load shifted")
    plt.axhline(
        metrics["peak_threshold"],
        linestyle="--",
        label="Peak threshold",
    )
    plt.title("Illustrative peak-shaving heuristic")
    plt.text(
        0,
        sample["energy"].max() * 0.95,
        f"Peak reduction: {metrics['peak_reduction_percent']:.1f}%",
    )
    plt.xlabel("Hour")
    plt.ylabel("Synthetic energy units")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=160)
    plt.close()

    print(f"Peak before: {metrics['peak_before']:.2f}")
    print(f"Peak after: {metrics['peak_after']:.2f}")
    print(
        "Peak reduction: "
        f"{metrics['peak_reduction_percent']:.2f}%"
    )
    print(
        "Energy balance error: "
        f"{metrics['energy_balance_error']:.8f}"
    )


if __name__ == "__main__":
    main()
