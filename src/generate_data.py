import numpy as np
import pandas as pd

np.random.seed(42)

hours = 24 * 120
time = pd.date_range("2024-01-01", periods=hours, freq="h")

df = pd.DataFrame({"timestamp": time})
df["hour"] = df["timestamp"].dt.hour

# features
df["temp"] = 10 + 10*np.sin(2*np.pi*df["hour"]/24) + np.random.randn(hours)
df["occupancy"] = np.where((df["hour"]>=8)&(df["hour"]<=18), 1, 0.3)

# energy
df["energy"] = (
    50
    + 40*df["occupancy"]
    + 3*np.abs(df["temp"]-18)
    + np.random.randn(hours)*3
)

df.to_csv("data/data.csv", index=False)
print("Dataset created")