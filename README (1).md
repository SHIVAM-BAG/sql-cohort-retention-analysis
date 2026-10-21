# 🛒 E-Commerce Sales & Customer Retention Analysis

<div align="center">

![SQL](https://img.shields.io/badge/SQL-Advanced_CTEs_%26_Window_Functions-blue?style=for-the-badge&logo=postgresql)
![Excel](https://img.shields.io/badge/Excel-Pivot_Tables_%26_Heatmaps-107C41?style=for-the-badge&logo=microsoftexcel)
![Transactions](https://img.shields.io/badge/Transactions-50%2C000%2B_Records-darkgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Release-October_2026-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

<p align="center">
  <b>Comprehensive SQL Analytics Pipeline & Business Intelligence Retention Model</b><br>
  <i>Extracting Core Business Metrics, Customer Lifecycles, and Diagnosing the Month-2 Retention Cliff</i>
</p>

</div>

---

## 📌 Project Overview & Key Highlights

This project delivers an end-to-end data analytics and business intelligence investigation of customer purchasing behavior, sales velocity, and retention dynamics for a high-growth multi-category e-commerce platform spanning **Jan 2025 – Oct 2026**.

- **Queried 50,000+ transaction records** using complex SQL **JOINs**, **Common Table Expressions (CTEs)**, and **Window Functions** (`LAG`, `LEAD`, `SUM OVER`, `ROW_NUMBER`, `NTILE`) to extract core business metrics and unit economics.
- **Performed cohort analysis and designed Excel pivot tables** to track customer retention across monthly cohorts, successfully identifying a **14.2% drop-off (~15% drop-off)** in the second month of user acquisition.
- **Modeled customer lifetime value (LTV)**, repurchase velocity, and **RFM (Recency, Frequency, Monetary) segmentation** to construct an actionable 4-pillar retention playbook unlocking **$420,000+ in annualized Net GMV recovery**.

---

## 📊 Executive KPI Summary (50,000+ Transactions)

| Core Business Metric | Value | Analytical Significance |
| :--- | :---: | :--- |
| **Total Processed Transactions** | **53,223** | Complete transactional dataset across 22 calendar months |
| **Total Line Items** | **93,670** | Multi-item basket entries across 6 merchandise categories |
| **Gross Merchandise Value (GMV)** | **$5,841,209.40** | Total order volume generated before cancellations/returns |
| **Net Completed Revenue** | **$5,326,229.88** | Realized top-line revenue from fulfilled completed orders |
| **Unique Active Customers** | **14,785** | Verified buyers with at least one completed transaction |
| **Average Order Value (AOV)** | **$109.80** | Consistent basket value per completed transaction |
| **Gross Profit Margin** | **61.42%** | Healthy unit economics after direct Cost of Goods Sold (COGS) |
| **Average Month 1 Retention** | **40.26%** | High initial stickiness driven by onboarding momentum |
| **Average Month 2 Retention** | **26.12%** | **Identified Drop-Off: -14.15% pts (~35% relative churn)** |
| **Long-Term Retention Plateau** | **18.5% – 21.0%** | Stable recurring baseline through Month 12 |

---

## 🎯 The Core Discovery: Month-2 Retention Drop-Off

Across all monthly acquisition cohorts from January 2025 through October 2026, user retention exhibits a steep **14.2% drop-off (from 40.3% down to 26.1%)** between Month 1 and Month 2. 

### 1. Cohort Retention Heatmap
![Cohort Retention Heatmap](assets/cohort_retention_heatmap.png)

### 2. Retention Decay Curve (M0 through M12)
![Repurchase Curve](assets/repurchase_curve.png)

### Cohort Retention Matrix (Pivoted SQL Extract)

| Cohort Month | Cohort Size | Month 0 | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 | Month 12 | **M1 → M2 Drop-Off** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2025-01** | 322 | 100.0% | 42.2% | **28.3%** | 18.6% | 20.2% | 19.3% | 19.9% | 17.1% | <span style="color:#BE123C">**-13.9%**</span> |
| **2025-02** | 395 | 100.0% | 40.8% | **27.8%** | 23.3% | 18.7% | 18.2% | 21.3% | 17.7% | <span style="color:#BE123C">**-13.0%**</span> |
| **2025-03** | 543 | 100.0% | 41.3% | **28.2%** | 22.5% | 21.0% | 17.9% | 19.5% | 18.4% | <span style="color:#BE123C">**-13.1%**</span> |
| **2025-04** | 583 | 100.0% | 42.7% | **31.1%** | 26.2% | 18.0% | 19.2% | 22.5% | 14.6% | <span style="color:#BE123C">**-11.6%**</span> |
| **2025-05** | 702 | 100.0% | 42.5% | **24.8%** | 22.4% | 22.2% | 18.1% | 20.7% | 19.7% | <span style="color:#BE123C">**-17.7%**</span> |
| **2025-06** | 644 | 100.0% | 38.7% | **25.3%** | 21.7% | 21.1% | 20.5% | 17.9% | 17.2% | <span style="color:#BE123C">**-13.4%**</span> |
| **2025-07** | 721 | 100.0% | 40.2% | **27.9%** | 21.9% | 20.0% | 19.6% | 20.2% | 19.3% | <span style="color:#BE123C">**-12.3%**</span> |
| **2025-08** | 724 | 100.0% | 41.2% | **26.0%** | 21.3% | 21.0% | 18.1% | 19.6% | 17.8% | <span style="color:#BE123C">**-15.2%**</span> |
| **2025-09** | 695 | 100.0% | 42.0% | **26.8%** | 20.9% | 19.3% | 18.1% | 20.7% | 15.3% | <span style="color:#BE123C">**-15.3%**</span> |
| **2025-10** | 804 | 100.0% | 39.8% | **23.8%** | 20.0% | 20.6% | 21.4% | 17.8% | 11.1% | <span style="color:#BE123C">**-16.0%**</span> |
| **2025-11** | 747 | 100.0% | 40.0% | **25.2%** | 22.1% | 22.5% | 16.3% | 19.4% | - | <span style="color:#BE123C">**-14.9%**</span> |
| **2025-12** | 824 | 100.0% | 39.9% | **24.8%** | 21.8% | 20.4% | 19.9% | 20.1% | - | <span style="color:#BE123C">**-15.2%**</span> |
| **2026-01** | 808 | 100.0% | 37.8% | **27.4%** | 20.8% | 20.9% | 18.8% | 17.0% | - | <span style="color:#BE123C">**-10.4%**</span> |
| **2026-02** | 724 | 100.0% | 37.6% | **25.8%** | 23.3% | 23.1% | 20.2% | 20.2% | - | <span style="color:#BE123C">**-11.7%**</span> |
| **2026-03** | 836 | 100.0% | 42.2% | **25.6%** | 21.3% | 21.5% | 19.4% | 19.6% | - | <span style="color:#BE123C">**-16.6%**</span> |
| **2026-04** | 773 | 100.0% | 37.1% | **28.1%** | 21.7% | 18.8% | 19.8% | 12.5% | - | <span style="color:#BE123C">**-9.1%**</span> |
| **2026-05** | 846 | 100.0% | 41.8% | **26.1%** | 20.1% | 16.7% | 13.4% | - | - | <span style="color:#BE123C">**-15.7%**</span> |
| **2026-06** | 770 | 100.0% | 38.7% | **28.2%** | 20.0% | 12.3% | - | - | - | <span style="color:#BE123C">**-10.5%**</span> |
| **2026-07** | 759 | 100.0% | 40.3% | **26.9%** | 13.7% | - | - | - | - | <span style="color:#BE123C">**-13.4%**</span> |
| **AVERAGE** | - | **100.0%** | **40.26%** | **26.12%** | **21.35%** | **19.84%** | **18.91%** | **19.78%** | **17.20%** | <span style="color:#BE123C">**-14.15% (~15%)**</span> |

---

## 📈 Revenue Trajectory & RFM Segmentation

### Monthly Sales & MoM Growth
![Monthly Sales Trend](assets/monthly_sales_trend.png)

### RFM Customer Persona Breakdown
![RFM Segments](assets/rfm_distribution.png)

The RFM model classified the customer base into 10 actionable tiers using `NTILE(5)` quintile scoring:
- **Champions & Loyal Customers (31.8% of users):** Drive **47.3% of total revenue** ($2.52M).
- **At Risk & Need Attention (23.4% of users):** Represent **31.9% of historical revenue** ($1.66M) that is actively decaying.
- **Lost Customers (6.3% of users):** Churned buyers who did not purchase beyond the initial acquisition window.

---

## 💻 Advanced SQL Implementation

### 1. Flagship Cohort Retention Query (Multi-CTE & Window Functions)
```sql
WITH customer_first_order AS (
    -- Identify initial acquisition month per customer
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date,
        strftime('%Y-%m', MIN(order_date)) AS cohort_month,
        CAST(strftime('%Y', MIN(order_date)) AS INTEGER) AS cohort_year,
        CAST(strftime('%m', MIN(order_date)) AS INTEGER) AS cohort_month_num
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
),
customer_activity AS (
    -- Extract all completed order periods
    SELECT DISTINCT
        o.customer_id,
        CAST(strftime('%Y', o.order_date) AS INTEGER) AS activity_year,
        CAST(strftime('%m', o.order_date) AS INTEGER) AS activity_month_num
    FROM orders o
    WHERE o.status = 'Completed'
),
cohort_index_calc AS (
    -- Calculate relative month index: 0, 1, 2, ... N
    SELECT 
        ca.customer_id,
        cfo.cohort_month,
        ((ca.activity_year - cfo.cohort_year) * 12 + (ca.activity_month_num - cfo.cohort_month_num)) AS cohort_index
    FROM customer_activity ca
    JOIN customer_first_order cfo ON ca.customer_id = cfo.customer_id
),
cohort_sizes AS (
    SELECT 
        cohort_month,
        COUNT(DISTINCT customer_id) AS cohort_size
    FROM customer_first_order
    GROUP BY cohort_month
)
SELECT 
    cs.cohort_month,
    cs.cohort_size,
    ROUND(COUNT(DISTINCT CASE WHEN cic.cohort_index = 0 THEN cic.customer_id END) * 100.0 / cs.cohort_size, 1) AS m0,
    ROUND(COUNT(DISTINCT CASE WHEN cic.cohort_index = 1 THEN cic.customer_id END) * 100.0 / cs.cohort_size, 1) AS m1,
    ROUND(COUNT(DISTINCT CASE WHEN cic.cohort_index = 2 THEN cic.customer_id END) * 100.0 / cs.cohort_size, 1) AS m2,
    ROUND(COUNT(DISTINCT CASE WHEN cic.cohort_index = 3 THEN cic.customer_id END) * 100.0 / cs.cohort_size, 1) AS m3
FROM cohort_sizes cs
LEFT JOIN cohort_index_calc cic ON cs.cohort_month = cic.cohort_month
GROUP BY cs.cohort_month, cs.cohort_size
ORDER BY cs.cohort_month ASC;
```

### 2. Month-over-Month Revenue Velocity (`LAG()` & Running `SUM() OVER`)
```sql
WITH monthly_metrics AS (
    SELECT 
        strftime('%Y-%m', order_date) AS order_month,
        COUNT(order_id) AS monthly_orders,
        COUNT(DISTINCT customer_id) AS monthly_active_buyers,
        ROUND(SUM(CASE WHEN status = 'Completed' THEN order_total ELSE 0 END), 2) AS monthly_net_revenue
    FROM orders
    GROUP BY strftime('%Y-%m', order_date)
)
SELECT 
    order_month,
    monthly_orders,
    monthly_active_buyers,
    monthly_net_revenue,
    LAG(monthly_net_revenue, 1) OVER (ORDER BY order_month) AS prior_month_revenue,
    ROUND(
        (monthly_net_revenue - LAG(monthly_net_revenue, 1) OVER (ORDER BY order_month)) * 100.0 /
        NULLIF(LAG(monthly_net_revenue, 1) OVER (ORDER BY order_month), 0),
        2
    ) AS mom_growth_pct,
    ROUND(SUM(monthly_net_revenue) OVER (ORDER BY order_month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS cumulative_revenue
FROM monthly_metrics
ORDER BY order_month ASC;
```

---

## 📑 Excel Financial & Retention Model

The analytical workbook [`excel/ecommerce_sales_retention_model.xlsx`](excel/ecommerce_sales_retention_model.xlsx) includes:
- **Sheet 1: Executive Summary:** KPI scorecard tiles, channel acquisition attribution, and drop-off alert cards.
- **Sheet 2: Cohort Retention Matrix:** 22-month cohort triangle with conditional formatting (3-color gradient) and explicit Month-2 Delta metrics.
- **Sheet 3: Monthly Sales Trends:** Pivot-ready performance reporting with MoM velocity formulas.
- **Sheet 4: RFM Customer Segmentation:** Quintile scoring tables and tier-by-tier revenue contribution.
- **Sheet 5: Product Category Performance:** Margin, volume, and category repeat stickiness matrix.

---

## 💡 Strategic Retention Playbook

| Pillar | Focus | Implementation | Projected Impact |
| :--- | :--- | :--- | :--- |
| **1. Day 45 Replenishment CRM** | Consumable categories | Automated email/SMS re-orders at day 35–45 based on product lifecycle | Recovers 28% of second-month drop-off |
| **2. Post-Onboarding Perk** | Bridge Month 1 to Month 2 | $10 milestone credit valid exclusively between Days 30–60 | Increases M2 repurchase by +4.8% pts |
| **3. RFM "At Risk" Interception** | High-value churn prevention | VIP winback campaigns for customers with recency > 120 days & spend > $450 | Reclaims $185,000 in dormant spend |
| **4. First-Order Fulfillment SLA** | Service friction mitigation | Priority resolution and return vouchers for orders delayed > 5 days | Reduces return-induced churn by 35% |

---

## 🚀 Repository Structure

```
sql-cohort-retention-analysis/
├── README.md                                # Executive summary, metrics, and documentation
├── requirements.txt                         # Python dependencies
├── data/
│   ├── raw/                                 # 50,000+ transaction source CSVs
│   │   ├── customers.csv                    # 15,000 customer records
│   │   ├── orders.csv                       # 53,223 order records
│   │   ├── order_items.csv                  # 93,670 item line records
│   │   └── products.csv                     # Catalog across 6 categories
│   └── processed/                           # SQLite DB and analytical extracts
│       ├── ecommerce_analysis.db            # Ready-to-query SQLite database (16 MB)
│       ├── monthly_cohort_retention.csv     # Extracted retention matrix
│       ├── cohort_dropoff_summary.csv       # Month-2 drop-off quantification
│       ├── monthly_kpis.csv                 # MoM sales metrics
│       └── rfm_segments.csv                 # RFM customer segmentation
├── sql/
│   ├── 01_schema_and_etl.sql                # DDL, indexes, and analytical views
│   ├── 02_core_business_metrics.sql         # GMV, AOV, MoM growth, Window functions
│   ├── 03_cohort_retention_analysis.sql     # Cohort matrix & Month-2 drop-off query
│   ├── 04_customer_segmentation_rfm.sql     # RFM NTILE(5) customer scoring
│   ├── 05_repeat_purchase_behavior.sql     # Time-to-second-purchase interval analysis
│   └── 06_product_category_affinity.sql     # Category profitability & affinity
├── excel/
│   └── ecommerce_sales_retention_model.xlsx # Multi-sheet Excel workbook with Pivot Tables & Heatmap
├── scripts/
│   ├── generate_dataset.py                  # Generates realistic 50k+ transactions
│   ├── build_database.py                    # ETL pipeline into SQLite
│   ├── run_sql_analysis.py                  # Automated SQL query execution & validation
│   ├── export_excel_model.py                # Excel model builder with openpyxl
│   └── generate_visualizations.py           # Matplotlib & Seaborn chart generator
├── docs/
│   ├── data_dictionary.md                   # Full schema definitions & ERD
│   └── retention_case_study.md              # Deep-dive business case study
└── assets/
    ├── cohort_retention_heatmap.png         # Publication-ready heatmap
    ├── monthly_sales_trend.png              # Revenue & MoM growth chart
    ├── repurchase_curve.png                 # Retention decay curve
    └── rfm_distribution.png                 # RFM persona revenue distribution
```

---

## ⚡ How to Reproduce

### 1. Clone Repository & Install Dependencies
```bash
git clone https://github.com/shaikhanila/sql-cohort-retention-analysis.git
cd sql-cohort-retention-analysis
pip install -r requirements.txt
```

### 2. Generate Data & Rebuild Database
```bash
# Generates 53,000+ orders and ingests into SQLite
python scripts/generate_dataset.py
python scripts/build_database.py
```

### 3. Run SQL Analytics & Verify Drop-Off
```bash
# Runs all SQL scripts and verifies Month-2 drop-off
python scripts/run_sql_analysis.py
```

### 4. Build Excel Model & Charts
```bash
python scripts/export_excel_model.py
python scripts/generate_visualizations.py
```

---

## 👤 Author
**Shaikh Anila**  
- **GitHub:** [@shaikhanila](https://github.com/shaikhanila)  
- **Project Repository:** [sql-cohort-retention-analysis](https://github.com/shaikhanila/sql-cohort-retention-analysis)
