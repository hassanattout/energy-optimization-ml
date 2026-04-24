# ⚡ Energy Consumption Prediction & Peak Optimization

Machine Learning • Energy Systems • Optimization

---

## 🚀 Overview

This project applies machine learning to predict building energy consumption and reduce peak demand through a simple yet effective optimization strategy.

---

## 💼 Why This Matters

Energy systems face critical challenges:

- High peak demand increases operational costs  
- Inefficient energy usage leads to waste  
- Load imbalance stresses infrastructure  

Machine learning enables smarter energy management by forecasting demand and optimizing usage.

---

## 🎯 Objective

- Predict hourly energy consumption  
- Reduce peak demand using optimization techniques  

---

## 🧠 Approach

- Generated hourly building dataset (temperature, occupancy)  
- Trained a **Random Forest Regressor**  
- Evaluated performance using RMSE (**≈ 3.5**)  
- Implemented a **peak-shaving strategy**  
- Compared energy usage before and after optimization  

---

## 📊 Results

- Accurate energy consumption prediction  
- Peak demand reduced by **~14%**  
- Improved load distribution over time  

---

## 📸 Visual Results

### Model Performance
![Energy Prediction](outputs/model.png)

### Optimization Impact
![Optimization Impact](outputs/optimization.png)

---

## 🧠 Methodology

- Generated hourly energy dataset (temperature, occupancy)  
- Performed feature engineering  
- Trained a Random Forest Regressor  
- Evaluated performance using RMSE  
- Applied peak-shaving optimization strategy  
- Compared results before and after optimization  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  

---

## 🧪 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/hassanattout/energy-optimization-ml.git
cd energy-optimization-ml
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python3 src/main.py
```

---

## 🗂️ Repository Structure
```text
energy-optimization-ml/
│
├── data/               # Dataset
├── models/             # Trained models
├── outputs/            # Results & visualizations
├── src/                # Source code
│
├── README.md
```

---

## 📌 Future Improvements

Use real-world datasets
Implement time-series models (LSTM, XGBoost)
Add real-time dashboard (Streamlit)
Improve optimization strategies

---

## 💡 Key Insight

Predicting energy consumption is useful.

👉 Optimizing it is where the real value lies.

---

## 👨‍💻 Author

Hassan Attout  
Machine Learning & Energy Systems  
LinkedIn: https://www.linkedin.com/in/hassanattout
