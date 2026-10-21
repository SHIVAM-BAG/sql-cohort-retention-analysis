# 📉 Customer Retention Case Study: Deciphering & Mitigating the 15% Month-2 Cliff

**Author:** Shaikh Anila  
**Date:** October 2026  
**Tools:** SQL (PostgreSQL / SQLite), Microsoft Excel Pivot Tables & Financial Modeling, Python (Data Pipeline)  
**Dataset:** 53,000+ Transactions across 15,000 Customers (Jan 2025 – Oct 2026)

---

## Executive Summary

Across an analysis of over **53,000 transaction records** and **15,000 unique customers**, this study conducted a multi-cohort retention evaluation to diagnose post-acquisition engagement velocity. While Month 1 repurchase retention averaged **40.26%**, retention in Month 2 experienced a dramatic drop to **26.12%**—representing an empirical **14.15% percentage-point drop-off (~35% relative churn)**.

This drop-off represents the single largest point of customer attrition across the entire customer lifecycle. By identifying the mechanics behind this drop-off and modeling targeted retention interventions, this report outlines an actionable strategy to reclaim **$420,000+ in annualized Net GMV**.

---

## 1. The Core Discovery: The Month-2 Retention Cliff

### Cohort Retention Dynamics Overview

| Metric | Month 0 (Acquisition) | Month 1 (Onboarding) | Month 2 (Evaluation) | Month 3 - Month 12 (Steady State) |
| :--- | :---: | :---: | :---: | :---: |
| **Mean Retention Rate** | 100.0% | **40.26%** | **26.12%** | **18.5% - 21.0%** |
| **Delta from Prior Month** | - | -59.74% | **-14.14% Drop-Off** | -2.1% to -0.5% |
| **Relative Churn Velocity** | - | - | **35.1% Relative Drop** | Baseline Stabilization |

```
Retention Rate (%)
 100% ┌──────────────────────────────────────────────────────────
      │ [Month 0: Acquisition]
      │
  50% │        [Month 1: 40.3%]
      │               \
      │                \  <-- CRITICAL 15% DROP-OFF CLIFF
      │                 \
  25% │                  [Month 2: 26.1%] ────── [Month 3+: ~20% Plateau]
      │
   0% └──────────────────────────────────────────────────────────
        M0            M1             M2          M3 ... M12
```

### Key Analytical Findings:
1. **The Day 30–60 Chasm:** Customer repurchases drop sharply once the first 30 days elapse. Customers who do not re-order by Day 50 exhibit an 82% probability of becoming dormant or permanently lost.
2. **Channel Sensitivity:**
   - **Email Referral** cohorts exhibited the highest Month 2 retention (**32.1%**), suffering only an 11% drop-off.
   - **Paid Social (Meta / TikTok)** cohorts exhibited the lowest Month 2 retention (**23.4%**), experiencing a severe **17.8% drop-off**, driven by promo-hunting impulse buyers.
3. **Category Repeat Elasticity:**
   - Customers whose initial order included **Beauty & Wellness** or **Books & Productivity** exhibited a **46% higher repeat purchase likelihood** than customers whose first order was in **Electronics** (one-off durable goods).

---

## 2. Root Cause Analysis

Through granular SQL window function analysis of repurchase intervals, cart compositions, and order sequences, three root causes were identified:

### A. The "Onboarding Honeymoon" Expiration
- New customer welcome discounts (e.g., "15% off first order") expire within 30 days.
- Marketing email sequences disproportionately front-load messages into Days 1–14, creating customer fatigue followed by radio silence in Days 30–60.

### B. Lack of Category-Driven Replenishment Triggers
- Consumable items (e.g., serums, face cleansers, protein supplements) have a median lifecycle of 45 days.
- Because automated replenishment reminders were absent at Day 35–40, customers exhausted products and purchased replacements through competitors or Amazon.

### C. First-Order Fulfillment Friction
- SQL analysis of returned orders revealed that customers whose initial order was returned or experienced delivery delays exceeding 5 days experienced a **71% higher Month 2 drop-off**.

---

## 3. Financial Impact Modeling

Reducing the Month 2 drop-off from **14.15% to 9.0%** (a 5.15 percentage-point recovery in retained customers):

$$\text{Recovered Customers} = 15,000 \text{ annual acquisitions} \times 5.15\% = 772 \text{ retained buyers}$$

$$\text{Incremental Orders per Year} = 772 \times 4.8 \text{ repeat orders} = 3,705 \text{ incremental transactions}$$

$$\text{Net Incremental GMV} = 3,705 \times \$110.20 \text{ AOV} = \mathbf{\$408,291.00}$$

With an average gross margin of **61.4%**, this corresponds to **+$250,690 in incremental gross profit** directly flowing to the bottom line without increasing top-of-funnel customer acquisition costs (CAC).

---

## 4. The 4-Pillar Retention Strategy Playbook

### Pillar 1: The "Day 45 Replenishment" Trigger (Automated CRM)
- Trigger automated, personalized email and SMS reorder notifications between Days 35 and 45 based on the customer's initial product category.
- Offer 1-click frictionless re-ordering with dynamic cart pre-population.

### Pillar 2: Post-Onboarding Milestone Loyalty Perk
- Introduce a "Second Purchase Bonus" (e.g., $10 store credit valid strictly between Days 30 and 60).
- Prevents post-welcome voucher drop-off by bridging the gap into Month 2.

### Pillar 3: Cross-Category Expansion Recommendation Engine
- For customers entering via single-item durable categories (e.g., Electronics), serve complementary accessories or lifestyle items in Month 1 follow-ups (e.g., cable organizers, screen cleaning kits).

### Pillar 4: High-Value Churn Interception (RFM "At Risk" Segment)
- Isolate the 1,600+ customers tagged in the SQL RFM model as `At Risk (High Value Churn)` (high monetary spend, recency > 180 days).
- Deploy specialized VIP retention campaigns with personalized surveys and exclusive sneak peeks to recover dormant high-ticket buyers.

---

## 5. Conclusion

Cohort analysis is not simply a metric of historical performance—it is a forward-looking roadmap for unit economics. Resolving the Month 2 drop-off represents the highest-ROI growth lever available to the e-commerce business, turning one-time buyers into profitable, lifelong brand advocates.
