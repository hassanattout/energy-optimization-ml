import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("data/data.csv")

X = df[["hour","temp","occupancy"]]
y = df["energy"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, pred))
print("RMSE:", rmse)

# plot
plt.scatter(y_test, pred, alpha=0.3)
m = max(y_test.max(), pred.max())
plt.plot([0,m],[0,m],'--')

plt.title("Predicted vs Actual Energy Consumption (Model Performance)")

# add RMSE on plot
plt.text(
    min(y_test),
    max(y_test)*0.9,
    f"RMSE: {rmse:.2f}",
)
plt.xlabel("Actual")
plt.ylabel("Predicted")

plt.savefig("outputs/model.png")
joblib.dump(model, "models/model.pkl")