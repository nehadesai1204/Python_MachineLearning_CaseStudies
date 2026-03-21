# 📊 Advertising Sales Prediction using Linear Regression

## 📌 Project Overview

This project demonstrates how to build a **Multiple Linear Regression model** to predict product **sales** based on advertising budgets across different media channels:

* TV
* Radio
* Newspaper

The workflow covers the complete machine learning pipeline—from data loading to model evaluation and visualization.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📂 Dataset

The dataset (`Advertising.csv`) contains advertising spend data and corresponding sales figures.

### Features:

* `TV`: Advertising budget spent on TV
* `radio`: Budget spent on radio ads
* `newspaper`: Budget spent on newspaper ads

### Target:

* `sales`: Sales achieved

---

## 🚀 Steps Performed

### 1. Load Dataset

* Reads the CSV file using Pandas
* Displays initial records

### 2. Data Cleaning

* Removes unnecessary columns like `Unnamed: 0` (if present)

### 3. Missing Value Check

* Identifies null values in dataset

### 4. Statistical Summary

* Uses `.describe()` to understand data distribution

### 5. Correlation Analysis

* Displays correlation matrix between features

### 6. Feature Selection

* Independent Variables: `TV`, `radio`, `newspaper`
* Dependent Variable: `sales`

### 7. Train-Test Split

* Splits data into:

  * 80% Training
  * 20% Testing

### 8. Model Training

* Uses **Linear Regression** from Scikit-learn

### 9. Prediction

* Predicts sales on test dataset

### 10. Model Evaluation

* Metrics used:

  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * R² Score

### 11. Coefficients

* Displays impact of each feature on sales

### 12. Result Comparison

* Compares actual vs predicted values

### 13. Visualization

* Scatter plot of actual vs predicted sales

---

## 📈 Output

* Model performance metrics
* Feature importance (coefficients)
* Visual comparison graph

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

2. Place `Advertising.csv` in the same directory.

3. Run the script:

```bash
python your_script_name.py
```

---

 📊 Sample Output Metrics

* Mean Squared Error
* Root Mean Squared Error
* R² Score (model accuracy)

---

## 🎯 Objective

To understand how advertising spending across different channels impacts product sales using a simple and interpretable machine learning model.

---

## 📌 Future Improvements

* Add feature scaling
* Try advanced models (Random Forest, XGBoost)
* Hyperparameter tuning
* Deploy model using Flask or Streamlit

---

## 👨‍💻 Author

Developed as part of a machine learning practice project.

---
