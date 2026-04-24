import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")

threshold = df["energy"].quantile(0.85)

df["optimized"] = df["energy"].copy()

peak = df["energy"] > threshold
df.loc[peak, "optimized"] *= 0.85

off_peak = df["energy"] < df["energy"].quantile(0.30)
shifted_energy = (df["energy"] - df["optimized"]).sum()

df.loc[off_peak, "optimized"] += shifted_energy / off_peak.sum()

sample = df.iloc[:200]

plt.figure(figsize=(10, 5))
plt.plot(sample["energy"], label="Original")
plt.plot(sample["optimized"], label="Optimized")
plt.axhline(threshold, linestyle="--", label="Peak threshold")
plt.title("Energy Optimization Impact (Peak Shaving)")
plt.text(
    0,
    max(sample["energy"])*0.95,
    f"Peak reduction: {peak_reduction:.1f}%",
)
plt.xlabel("Hour")
plt.ylabel("Energy Consumption")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/optimization.png")

peak_before = df["energy"].max()
peak_after = df["optimized"].max()
peak_reduction = ((peak_before - peak_after) / peak_before) * 100

print(f"Peak before: {peak_before:.2f}")
print(f"Peak after: {peak_after:.2f}")
print(f"Peak reduction: {peak_reduction:.2f}%")
print("Saved plot to outputs/optimization.png")