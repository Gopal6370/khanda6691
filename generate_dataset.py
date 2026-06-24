import pandas as pd
import random
from datetime import datetime, timedelta

cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad",
    "Chennai", "Kolkata", "Pune", "Ahmedabad"
]

categories = [
    "Electronics",
    "Fashion",
    "Beauty",
    "Home Decor",
    "Groceries"
]

genders = ["Male", "Female"]

data = []

start_date = datetime(2025, 1, 1)

for i in range(1, 1001):

    order_id = f"O{i:04d}"
    customer_id = f"C{i:04d}"

    gender = random.choice(genders)
    age = random.randint(18, 60)
    city = random.choice(cities)
    category = random.choice(categories)

    if category == "Electronics":
        amount = random.randint(8000, 30000)
    elif category == "Fashion":
        amount = random.randint(1000, 8000)
    elif category == "Beauty":
        amount = random.randint(500, 5000)
    elif category == "Home Decor":
        amount = random.randint(2000, 12000)
    else:
        amount = random.randint(500, 4000)

    order_date = start_date + timedelta(days=random.randint(0, 364))

    data.append([
        order_id,
        customer_id,
        gender,
        age,
        city,
        category,
        amount,
        order_date.strftime("%Y-%m-%d")
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Customer_ID",
    "Gender",
    "Age",
    "City",
    "Category",
    "Purchase_Amount",
    "Order_Date"
])

df.to_csv("ecommerce_data.csv", index=False)

print("Dataset Generated Successfully!")
print("Total Records:", len(df))
print(df.head())