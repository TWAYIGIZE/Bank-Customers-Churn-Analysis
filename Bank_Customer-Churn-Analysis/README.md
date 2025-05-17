# Customer Churn Analysis (No Machine Learning)

This project performs **exploratory data analysis (EDA)** to understand the key drivers of customer churn in a banking dataset. It uses Python libraries such as **Pandas**, **Matplotlib**, **Seaborn**, and **SciPy** to generate insights from the data.

---

## 📁 Dataset
The dataset used is assumed to be in CSV format and contains customer information including:
- `CreditScore`
- `Geography`
- `Gender`
- `Age`
- `Tenure`
- `Balance`
- `NumOfProducts`
- `IsActiveMember`
- `EstimatedSalary`
- `Exited` (target column: 1 = churned, 0 = stayed)

You must update the path to your own dataset in this line:
```python
data_path = r"C:/Users/LENOVO/.../Bank_Churn.csv"
```

---

## 📌 Objectives Covered

### 1. **Customer Churn Overview**
- Count plot to see number of churned vs non-churned customers
- Pie chart to visualize churn percentage

### 2. **Demographic Impact**
- Churn by gender
- Churn by geography
- Age distribution and its relation to churn

### 3. **Customer Behavior**
- Tenure vs churn (boxplot)
- Number of products vs churn
- Active member status and churn

### 4. **Financial Factors**
- Credit Score vs churn
- Account Balance vs churn
- Estimated Salary vs churn

### 5. **Correlation Analysis**
- Heatmap of key numerical variables
- Pearson correlation between credit score and churn

---

## 🛠️ Tools & Libraries
- **Pandas**: Data manipulation
- **Matplotlib**: Basic plotting
- **Seaborn**: Statistical visualizations
- **SciPy**: Statistical correlation test (Pearson)

---

## 📊 How to Run
1. Install required libraries:
```bash
pip install pandas matplotlib seaborn scipy
```
2. Run the script in any Python environment (Jupyter Notebook, VS Code, etc.)
3. View printed outputs and visualizations to understand churn patterns

---

## 💡 Key Insights You Can Extract
- Which demographics are most likely to churn
- Whether financial factors (balance, salary) influence churn
- Impact of account tenure, number of products, and activity

---

## 🧠 Notes
This project does **not use machine learning**. It is purely for **descriptive analysis** and **visual storytelling** to understand customer behavior.

For predictive analysis, you can build on this EDA and apply models like **Logistic Regression**, **Random Forest**, etc.

---

## 📎 Optional Extensions
- Export dashboard to PDF
- Connect to Power BI for interactive visualization
- Add feature engineering for ML model training

---

**Author:** *(Gaba Twayigize)*  
