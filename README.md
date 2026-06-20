# 🛒 E-Commerce Sales & Customer Behavior Analytics Pipeline

A self-contained, production-ready Python pipeline that simulates a realistic e-commerce dataset and performs end-to-end **sales analytics** and **customer segmentation** — with **zero external data files** required.

The entire dataset (customers, products, orders, prices, dates) is **synthetically generated in-memory** using NumPy and Pandas, complete with intentionally injected data-quality issues (missing values, duplicates) so the pipeline can demonstrate real-world cleaning logic.

---

## 📋 Overview

This project simulates the kind of analytics workflow a Data Science / Analytics Engineering team would run against a real e-commerce orders table:

1. **Synthetic Data Generation** — realistic customers, product categories, prices, order dates, payment methods, and discounts, generated with NumPy's random generators.
2. **Data Cleaning** — duplicate removal and missing-value imputation using group-aware statistics.
3. **Business Metrics** — total revenue, average order value, top-selling categories, monthly sales trends (with month-over-month growth), payment method and membership-tier breakdowns.
4. **Customer Segmentation** — quartile-based (RFM-style) segmentation by spending level and purchase frequency, classifying customers into segments such as `Champions`, `Loyal Customers`, `Big Spenders`, `Potential`, and `At Risk`.
5. **Console Reporting** — a clean, structured, business-readable report printed directly to the terminal.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core language, type hints, dataclasses |
| **Pandas** | DataFrame manipulation, grouping/aggregation, time-series resampling, `qcut` quantile binning |
| **NumPy** | Random number generation (`default_rng`), vectorized math, `digitize` binning, array operations |
| **Python `logging`** | Pipeline execution tracing (generation, cleaning, metrics, segmentation steps) |

No external CSV/Excel files, databases, or third-party data sources are required — the project is fully self-contained and runs anywhere Python, Pandas, and NumPy are installed.

---

## 📁 Project Structure

```
ecommerce-analytics-pipeline/
│
├── ecommerce_analytics_pipeline.py   # Full pipeline: generation, cleaning, metrics, segmentation, reporting
├── README.md                         # Project documentation (this file)
└── requirements.txt                  # Python dependencies (pandas, numpy)
```

---

## ⚙️ Installation & Execution

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/ecommerce-analytics-pipeline.git
cd ecommerce-analytics-pipeline
```

### Step 2 — Create a virtual environment (recommended)
```bash
python3 -m venv venv

# Activate the environment
# macOS / Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

`requirements.txt` contains:
```
pandas>=2.0
numpy>=1.24
```

### Step 4 — Run the pipeline
```bash
python ecommerce_analytics_pipeline.py
```

That's it — no data files to download or configure. The script generates its own dataset, cleans it, computes KPIs, segments customers, and prints a full report to the console.

### Optional — Use the pipeline programmatically
```python
from ecommerce_analytics_pipeline import run_pipeline, PipelineConfig

# Customize dataset size / date range if desired
config = PipelineConfig(n_customers=1000, n_orders=8000)
clean_df, metrics, customer_segments = run_pipeline(config)

# clean_df            -> full cleaned transactional DataFrame
# metrics              -> dict of KPI tables (category_summary, monthly_summary, etc.)
# customer_segments    -> one row per customer with segment labels
```

---

## 📊 Sample Console Output

Below is an abbreviated sample of the report printed when running the pipeline (values vary slightly between configurations but follow this exact structure):

```
========================================================================
 E-COMMERCE SALES & CUSTOMER BEHAVIOR ANALYTICS REPORT
========================================================================

[1] DATASET OVERVIEW
------------------------------------------------------------------------
Total Cleaned Records   : 6,000
Unique Customers        : 799
Unique Product Categories: 8
Date Range              : 2023-01-01 -> 2024-12-31

[2] CORE BUSINESS METRICS
------------------------------------------------------------------------
Total Revenue           : $5,780,861.28
Total Orders            : 6,000
Average Order Value     : $963.48

[3] TOP-SELLING PRODUCT CATEGORIES (by Revenue)
------------------------------------------------------------------------
                        total_revenue  total_units_sold  avg_order_value  order_count  revenue_share_pct
product_category
Electronics              3,829,317.89               3929         2,912.03         1315              66.24
Home & Kitchen              724,554.34              2460           895.62          809              12.53
Apparel                     427,824.65              3337           396.50         1079               7.40
Sports & Outdoors           382,590.43              1769           656.24          583               6.62
Beauty & Personal Care       189,297.94              2471           226.70          835               3.27
Toys & Games                 122,711.18              1212           304.49          403               2.12
Books                         61,690.99              1491           124.63          495               1.07
Groceries                     42,873.86              1465            89.13          481               0.74

[4] MONTHLY SALES TREND
------------------------------------------------------------------------
             monthly_revenue  order_count  avg_order_value  mom_growth_pct
order_month
2023-01           233,173.95          266           876.59             NaN
2023-02           206,334.06          219           942.16          -11.51
2023-03           213,287.38          239           892.42            3.37
2023-04           266,048.01          258         1,031.19           24.74
2023-05           270,055.51          255         1,059.04            1.51
... (14 months omitted) ...
2024-08           244,460.08          254           962.44           -9.13
2024-09           187,215.12          211           887.28          -23.42
2024-10           271,766.29          254         1,069.95           45.16
2024-11           199,338.78          232           859.22          -26.65
2024-12           267,455.44          251         1,065.56           34.17

[5] REVENUE BY PAYMENT METHOD
------------------------------------------------------------------------
payment_method
Credit Card        2,261,281.39
Debit Card         1,245,120.38
PayPal              1,179,332.14
Cash on Delivery       562,963.87
Bank Transfer          532,163.50

[6] REVENUE BY MEMBERSHIP TIER
------------------------------------------------------------------------
                 total_revenue  avg_order_value  order_count
membership_tier
Bronze             2,638,652.89           958.46         2753
Silver              1,660,543.33         1,006.39         1650
Gold                  970,015.94           885.05         1096
Platinum              511,649.12         1,021.26          501

[7] CUSTOMER SEGMENTATION SUMMARY
------------------------------------------------------------------------
                  customer_count  avg_total_spend  avg_purchase_frequency
customer_segment
Champions                    271        11,971.04                   10.11
Big Spenders                 128         9,411.65                    5.84
Potential                     58         4,469.61                    6.43
Loyal Customers               128         4,144.86                    8.85
At Risk                       214         2,533.82                    4.70

[8] SPENDING TIER DISTRIBUTION
------------------------------------------------------------------------
spending_tier
Premium    200
High       199
Medium     200
Low        200

[9] SAMPLE: TOP 5 CUSTOMERS BY TOTAL SPEND
------------------------------------------------------------------------
 customer_id  total_spend  purchase_frequency customer_segment spending_tier membership_tier
         210    27,277.42                  11        Champions       Premium          Silver
         653    26,887.99                  11        Champions       Premium          Silver
         423    25,778.44                  16        Champions       Premium            Gold
         704    24,270.23                  13        Champions       Premium          Bronze
         444    23,138.18                  12        Champions       Premium          Bronze

========================================================================
 END OF REPORT
========================================================================
```

---

## 🧩 Pipeline Architecture

| Function | Responsibility |
|---|---|
| `generate_synthetic_dataset()` | Builds customer master data and order transactions using NumPy `default_rng`; injects missing values and duplicate rows |
| `clean_dataset()` | Drops duplicates, imputes missing prices/quantities/cities, recalculates `total_amount` net of discounts |
| `calculate_business_metrics()` | Computes total revenue, AOV, category leaderboards, monthly trend with MoM growth, payment & tier breakdowns |
| `segment_customers()` | Aggregates per-customer spend/frequency, applies quartile scoring (`pd.qcut`) and NumPy `digitize` binning to assign segments and spending tiers |
| `print_report()` | Formats and prints the full console report |
| `run_pipeline()` | Orchestrates the entire flow end-to-end and returns the cleaned data, metrics, and segments |

All randomness is seeded (`random_seed=42` by default) for reproducible results across runs.

---

## 📈 Customer Segmentation Logic

Customers are scored on two dimensions using quartile binning (`pd.qcut`):

- **Monetary Score (1–4):** based on total historical spend
- **Frequency Score (1–4):** based on number of orders placed

| Monetary | Frequency | Segment |
|---|---|---|
| High (≥3) | High (≥3) | **Champions** |
| Low (<3) | High (≥3) | **Loyal Customers** |
| High (≥3) | Low (<3) | **Big Spenders** |
| Mid (=2) | Mid (=2) | **Potential** |
| Low | Low | **At Risk** |

A separate `spending_tier` (`Low` / `Medium` / `High` / `Premium`) is derived independently using `np.digitize` against spend quartiles.

---

## 🔧 Customization

All dataset parameters are controlled via the `PipelineConfig` dataclass:

```python
@dataclass(frozen=True)
class PipelineConfig:
    n_customers: int = 800
    n_orders: int = 6000
    start_date: str = "2023-01-01"
    end_date: str = "2024-12-31"
    missing_value_fraction: float = 0.03
    duplicate_fraction: float = 0.02
    random_seed: int = 42
```

Adjust any of these values to scale the dataset up/down or change the simulated time range.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to fork, modify, and extend it.
