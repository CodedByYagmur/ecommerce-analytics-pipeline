# E-Commerce Data Analysis
# A simple project that creates a small dataset and analyzes it using Pandas and NumPy

import pandas as pd
import numpy as np

# -----------------------------------------
# STEP 1: Create a simple dataset using a dictionary
# -----------------------------------------
# I made up 25 orders with some basic info about each one

data = {
    "OrderID": list(range(1, 26)),
    "Product": [
        "Laptop", "T-Shirt", "Headphones", "Novel Book", "Sneakers",
        "Coffee Mug", "Smartphone", "Backpack", "Desk Lamp", "Notebook",
        "Wireless Mouse", "Jeans", "Water Bottle", "Tablet", "Sunglasses",
        "Keyboard", "Hoodie", "Cookbook", "Running Shoes", "Phone Case",
        "Monitor", "Jacket", "Pen Set", "Earbuds", "Bookshelf"
    ],
    "Category": [
        "Electronics", "Clothing", "Electronics", "Books", "Clothing",
        "Home", "Electronics", "Clothing", "Home", "Books",
        "Electronics", "Clothing", "Home", "Electronics", "Clothing",
        "Electronics", "Clothing", "Books", "Clothing", "Electronics",
        "Electronics", "Clothing", "Books", "Electronics", "Home"
    ],
    "Price": [
        899.99, 15.99, 59.99, 12.50, 75.00,
        9.99, 699.00, 45.00, np.nan, 6.99,
        25.50, 39.99, 14.99, 320.00, 18.00,
        49.99, 34.99, np.nan, 89.99, 12.99,
        199.99, 65.00, 8.50, 29.99, 120.00
    ],
    "Quantity": [
        1, 3, 2, 1, 1,
        4, 1, 2, 1, 5,
        2, 1, 3, 1, 2,
        1, 2, 2, 1, np.nan,
        1, 1, 4, 2, 1
    ]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

print("----- Original Dataset -----")
print(df)
print("\n")

# -----------------------------------------
# STEP 2: Check for missing values
# -----------------------------------------
# .isnull().sum() tells us how many missing values are in each column

print("----- Missing Values Before Cleaning -----")
print(df.isnull().sum())
print("\n")

# -----------------------------------------
# STEP 3: Clean the data using fillna()
# -----------------------------------------
# For Price, we fill missing values with the average price
# For Quantity, we fill missing values with 1 (assuming at least 1 item was bought)

average_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(round(average_price, 2))
df["Quantity"] = df["Quantity"].fillna(1)

print("----- Missing Values After Cleaning -----")
print(df.isnull().sum())
print("\n")

# -----------------------------------------
# STEP 4: Calculate Total Revenue per order
# -----------------------------------------
# We add a new column called "Revenue" which is Price * Quantity

df["Revenue"] = df["Price"] * df["Quantity"]
df["Revenue"] = df["Revenue"].round(2)

print("----- Dataset with Revenue Column -----")
print(df)
print("\n")

# -----------------------------------------
# STEP 5: Calculate basic business metrics
# -----------------------------------------

# Total revenue from all orders combined
total_revenue = df["Revenue"].sum()

# Average value of a single order
average_order_value = df["Revenue"].mean()

# Find the top-selling category by total revenue using groupby
category_revenue = df.groupby("Category")["Revenue"].sum()
top_category = category_revenue.idxmax()
top_category_value = category_revenue.max()

# -----------------------------------------
# STEP 6: Print a simple summary report
# -----------------------------------------

print("===========================================")
print("        E-COMMERCE ANALYSIS SUMMARY")
print("===========================================")
print(f"Total Number of Orders: {len(df)}")
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Order Value: ${average_order_value:.2f}")
print("\nRevenue by Category:")
print(category_revenue)
print(f"\nTop-Selling Category: {top_category} (${top_category_value:.2f})")
print("===========================================")
