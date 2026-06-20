# E-Commerce Data Analysis

A simple Python project that analyzes sample e-commerce order data using Pandas and NumPy. This was made as a practice project to learn basic data cleaning and analysis with Pandas.

## What This Project Does

- Creates a small sample dataset (25 orders) using a Python dictionary
- Converts the dictionary into a Pandas DataFrame
- Cleans the data by filling in missing values with `.fillna()`
- Calculates total revenue for each order (Price × Quantity)
- Finds total revenue, average order value, and the top-selling category

## Technologies Used

- Python 3
- Pandas
- NumPy

## Project Structure

```
ecommerce-data-analysis/
│
├── ecommerce_analysis.py   # main script
└── README.md                # this file
```

## How to Run It

1. Make sure you have Python installed (3.8 or higher works fine).
2. Install the required libraries:

```bash
pip install pandas numpy
```

3. Run the script:

```bash
python ecommerce_analysis.py
```

That's it — no extra files needed. The dataset is built right inside the script.

## What the Dataset Looks Like

The dataset has 25 rows and these columns:

| Column   | Description                          |
|----------|---------------------------------------|
| OrderID  | A unique number for each order        |
| Product  | Name of the product                   |
| Category | Electronics, Clothing, Books, or Home |
| Price    | Price of one item                     |
| Quantity | How many items were ordered           |

I also added a few missing values (NaN) on purpose — 2 in Price and 1 in Quantity — to practice cleaning data with `.fillna()`.

## How the Data is Cleaned

- Missing **Price** values are filled with the **average price** of all products.
- Missing **Quantity** values are filled with **1**, assuming at least one item was bought.

## Example Output

Here is a part of what the script prints when you run it:

```
===========================================
        E-COMMERCE ANALYSIS SUMMARY
===========================================
Total Number of Orders: 25
Total Revenue: $3585.53
Average Order Value: $143.42

Revenue by Category:
Category
Books           329.65
Clothing        513.93
Electronics    2412.92
Home            329.03
Name: Revenue, dtype: float64

Top-Selling Category: Electronics ($2412.92)
===========================================
```

## What I Learned

- How to build a DataFrame from a Python dictionary
- How to check for and fill missing values with `.fillna()`
- How to create a new column using basic math on existing columns
- How to use `.groupby()` to summarize data by category
- How to find the max value in a grouped Series using `.idxmax()`

## Notes

This is a beginner-level project for practicing Pandas basics, so the code is kept simple on purpose (no functions, no classes, just a straightforward top-to-bottom script).
