# 1. Importing Libraries
import pandas as pd  # For data manipulation
import matplotlib.pyplot as plt  # For plotting basic charts
import seaborn as sns  # For advanced visualizations
from scipy.stats import pearsonr  # For statistical correlation (Pearson)

# 2. Loading Dataset
data_path = r"C:/Users/LENOVO/Downloads/Customer-Churn-Analysis-main/Customer-Churn-Analysis-main/Bank_Customers_Churn.csv"
df = pd.read_csv(data_path)
print("Dataset successfully loaded.\n")

# 3. Basic Info and Description
print("Data Info:")
print(df.info())  # Show column types, non-null counts
print("\nData Summary:")
print(df.describe())  # Summary statistics of numeric columns

# 4. Check Missing Values
missing = df.isnull().sum()
print("\nMissing values per column:\n", missing)

# ========== OBJECTIVE 1: Customer Churn Overview ==========

# 5. Bar chart: Churn count
distribution_plot = sns.countplot(data=df, x='Exited', color='brown')
plt.title('Customer Churn Distribution')
plt.xlabel('Exited (0 = Stayed, 1 = Churned)')
plt.ylabel('Count')
plt.show()

# 6. Pie chart: Churn proportion
labels = ['Stayed', 'Churned']
values = df['Exited'].value_counts()
colors = ['orange', '#66b3ff']
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
plt.title('Churn Percentage')
plt.show()

# ========== OBJECTIVE 2: Demographic Impact ==========

# 7. Gender vs Churn
sns.countplot(data=df, x='Gender', hue='Exited', palette='pastel')
plt.title('Churn by Gender')
plt.show()

# 8. Geography vs Churn
sns.countplot(data=df, x='Geography', hue='Exited', palette='muted')
plt.title('Churn by Geography')
plt.show()

# 9. Age distribution by Churn
sns.histplot(data=df, x='Age', hue='Exited', bins=20, kde=True)
plt.title('Age Distribution by Churn')
plt.show()

# ========== OBJECTIVE 3: Customer Behavior ==========

# 10. Tenure vs Churn
sns.boxplot(data=df, x='Exited', y='Tenure')
plt.title('Tenure vs Churn')
plt.show()

# 11. Products vs Churn
sns.countplot(data=df, x='NumOfProducts', hue='Exited', palette='deep')
plt.title('Number of Products vs Churn')
plt.show()

# 12. Active Member vs Churn
sns.countplot(data=df, x='IsActiveMember', hue='Exited', palette='coolwarm')
plt.title('Active Membership vs Churn')
plt.show()

# ========== OBJECTIVE 4: Financial Factors ==========

# 13. Credit Score vs Churn
sns.boxplot(data=df, x='Exited', y='CreditScore')
plt.title('Credit Score vs Churn')
plt.show()

# 14. Balance vs Churn
sns.boxplot(data=df, x='Exited', y='Balance')
plt.title('Account Balance vs Churn')
plt.show()

# 15. Estimated Salary vs Churn
sns.boxplot(data=df, x='Exited', y='EstimatedSalary')
plt.title('Estimated Salary vs Churn')
plt.show()

# ========== CORRELATION ANALYSIS ==========

# 16. Heatmap of correlations
cols_to_check = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary', 'Exited']
corr_matrix = df[cols_to_check].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
plt.title("Feature Correlation Heatmap")
plt.show()

# 17. Pearson correlation between Credit Score and Churn
pearson_score, _ = pearsonr(df['CreditScore'], df['Exited'])
print(f"\nPearson Correlation between Credit Score and Churn: {pearson_score:.2f}")
