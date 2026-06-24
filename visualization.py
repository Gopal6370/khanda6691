import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder automatically
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("ecommerce_data.csv")

# Convert date column to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

sns.set_style("whitegrid")

# ==========================
# 1. Sales by Category
# ==========================
plt.figure(figsize=(10,6))

category_sales = df.groupby("Category")["Purchase_Amount"].sum().sort_values(ascending=False)

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Total Sales by Category", fontsize=16)
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("images/category_sales.png")
plt.show()

# ==========================
# 2. Sales by City
# ==========================
plt.figure(figsize=(10,6))

city_sales = df.groupby("City")["Purchase_Amount"].sum().sort_values(ascending=False)

sns.barplot(
    x=city_sales.index,
    y=city_sales.values
)

plt.title("Total Sales by City", fontsize=16)
plt.xlabel("City")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/city_sales.png")
plt.show()

# ==========================
# 3. Age Distribution
# ==========================
plt.figure(figsize=(10,6))

sns.histplot(
    df["Age"],
    bins=10,
    kde=True
)

plt.title("Customer Age Distribution", fontsize=16)
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("images/age_distribution.png")
plt.show()

# ==========================
# 4. Monthly Sales Trend
# ==========================
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Purchase_Amount"].sum()

plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("images/monthly_sales_trend.png")
plt.show()

# ==========================
# 5. Gender Spending Comparison
# ==========================
plt.figure(figsize=(8,6))

sns.boxplot(
    x="Gender",
    y="Purchase_Amount",
    data=df
)

plt.title("Gender Spending Comparison", fontsize=16)
plt.xlabel("Gender")
plt.ylabel("Purchase Amount")

plt.tight_layout()
plt.savefig("images/gender_spending_comparison.png")
plt.show()

print("="*50)
print("All charts generated successfully!")
print("="*50)

print("Generated Files:")
print("1. category_sales.png")
print("2. city_sales.png")
print("3. age_distribution.png")
print("4. monthly_sales_trend.png")
print("5. gender_spending_comparison.png")
