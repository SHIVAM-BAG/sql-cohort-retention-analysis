"""
Generates publication-quality charts and visualizations for the project
and saves them to assets/.
"""

import os
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Styling configuration
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'Helvetica', 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#E2E8F0'
plt.rcParams['axes.linewidth'] = 0.8

# 1. COHORT RETENTION HEATMAP
def plot_cohort_heatmap():
    csv_path = os.path.join(PROCESSED_DIR, "monthly_cohort_retention.csv")
    df = pd.read_csv(csv_path)
    
    # Filter cohorts up to 2026-06 to show mature cohorts
    df_mature = df[df["cohort_month"] <= "2026-06"].copy()
    
    cohort_months = df_mature["cohort_month"].values
    retention_cols = [f"m{i}" for i in range(13)]
    matrix_data = df_mature[retention_cols].values
    
    # Mask zeroes (future months)
    mask = matrix_data == 0
    
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    
    cmap = sns.color_palette("mako_r", as_cmap=True)
    sns.heatmap(
        matrix_data, 
        annot=True, 
        fmt=".1f", 
        cmap="YlGnBu", 
        mask=mask,
        cbar_kws={'label': 'Retention Rate (%)', 'shrink': 0.8},
        xticklabels=[f"M{i}" for i in range(13)],
        yticklabels=cohort_months,
        linewidths=0.5,
        linecolor="#F1F5F9",
        ax=ax,
        annot_kws={"size": 9, "weight": "bold"}
    )
    
    ax.set_title("E-Commerce Monthly Customer Cohort Retention Matrix (2025 - 2026)\nNoticeable ~15% Drop-Off From Month 1 to Month 2", fontsize=14, weight="bold", pad=15, color="#0F172A")
    ax.set_xlabel("Cohort Month Index (M0 = Acquisition Month)", fontsize=11, weight="bold", color="#334155")
    ax.set_ylabel("Cohort Acquisition Month", fontsize=11, weight="bold", color="#334155")
    
    # Highlight Month 1 to Month 2 drop-off boundary
    ax.axvline(x=2, color="#E11D48", linestyle="--", linewidth=1.5, alpha=0.8)
    ax.text(2.05, 0.5, "15% Drop-Off Cliff", color="#BE123C", weight="bold", fontsize=10, rotation=270, va="top")
    
    plt.tight_layout()
    output_file = os.path.join(ASSETS_DIR, "cohort_retention_heatmap.png")
    plt.savefig(output_file)
    plt.close()
    print(f"Saved: {output_file}")

# 2. MONTHLY REVENUE & MOM GROWTH TREND
def plot_monthly_sales_trend():
    csv_path = os.path.join(PROCESSED_DIR, "monthly_kpis.csv")
    df = pd.read_csv(csv_path)
    
    fig, ax1 = plt.subplots(figsize=(12, 6), dpi=300)
    
    months = df["order_month"].values
    revenue = df["monthly_net_revenue"].values / 1000.0 # in $K
    growth = df["mom_growth_pct"].fillna(0).values
    
    # Bar chart for revenue
    color_bar = "#2563EB"
    bars = ax1.bar(months, revenue, color=color_bar, alpha=0.85, width=0.6, label="Monthly Revenue ($k)")
    ax1.set_ylabel("Net Completed Revenue ($K)", fontsize=11, weight="bold", color=color_bar)
    ax1.set_xlabel("Order Month", fontsize=11, weight="bold", color="#334155")
    ax1.tick_params(axis='y', labelcolor=color_bar)
    ax1.set_xticklabels(months, rotation=45, ha='right', fontsize=9)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Line chart for MoM growth
    ax2 = ax1.twinx()
    color_line = "#059669"
    ax2.plot(months, growth, color=color_line, marker="o", linewidth=2.2, label="MoM Growth (%)")
    ax2.set_ylabel("Month-over-Month Growth (%)", fontsize=11, weight="bold", color=color_line)
    ax2.tick_params(axis='y', labelcolor=color_line)
    ax2.axhline(0, color="#94A3B8", linestyle="--", linewidth=0.8)
    ax2.grid(False)
    
    plt.title("E-Commerce Monthly Net Revenue & MoM Growth Trajectory (50,000+ Orders)", fontsize=13, weight="bold", pad=15, color="#0F172A")
    plt.tight_layout()
    output_file = os.path.join(ASSETS_DIR, "monthly_sales_trend.png")
    plt.savefig(output_file)
    plt.close()
    print(f"Saved: {output_file}")

# 3. AVERAGE RETENTION DECAY CURVE (MONTH 0 - MONTH 12)
def plot_retention_decay_curve():
    csv_path = os.path.join(PROCESSED_DIR, "monthly_cohort_retention.csv")
    df = pd.read_csv(csv_path)
    
    # Use cohorts up to 2025-10 so we have 12 full months
    df_12m = df[df["cohort_month"] <= "2025-10"].copy()
    retention_cols = [f"m{i}" for i in range(13)]
    avg_retention = df_12m[retention_cols].mean().values
    
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    indices = np.arange(13)
    
    ax.plot(indices, avg_retention, marker='o', markersize=7, color="#1E3A8A", linewidth=2.5, label="Average Retention Rate (%)")
    
    # Annotate points
    for idx, val in enumerate(avg_retention):
        offset = (0, 7) if idx != 2 else (0, -18)
        color = "#BE123C" if idx in [1, 2] else "#1E293B"
        weight = "bold" if idx in [1, 2] else "normal"
        ax.annotate(f"{val:.1f}%", (idx, val), textcoords="offset points", xytext=offset, ha='center', fontsize=9, weight=weight, color=color)
        
    # Draw drop-off arrow between M1 and M2
    m1_val = avg_retention[1]
    m2_val = avg_retention[2]
    diff = m1_val - m2_val
    ax.annotate(
        f"Critical Drop-Off:\n-{diff:.1f}% pts in Month 2",
        xy=(1.5, (m1_val + m2_val) / 2),
        xytext=(2.8, 48),
        arrowprops=dict(facecolor="#BE123C", shrink=0.08, width=1.5, headwidth=7),
        fontsize=10,
        weight="bold",
        color="#BE123C",
        bbox=dict(boxstyle="round,pad=0.4", fc="#FFE4E6", ec="#BE123C", lw=1)
    )
    
    ax.set_title("Customer Retention Decay Curve: Quantifying the Month-2 Acquisition Cliff", fontsize=13, weight="bold", pad=15, color="#0F172A")
    ax.set_xlabel("Cohort Month Index (M0 = Acquisition Month)", fontsize=11, weight="bold", color="#334155")
    ax.set_ylabel("Retention Rate (% of Cohort)", fontsize=11, weight="bold", color="#334155")
    ax.set_xticks(indices)
    ax.set_xticklabels([f"Month {i}" for i in range(13)])
    ax.set_ylim(0, 110)
    ax.grid(True, linestyle="--", alpha=0.6)
    
    plt.tight_layout()
    output_file = os.path.join(ASSETS_DIR, "repurchase_curve.png")
    plt.savefig(output_file)
    plt.close()
    print(f"Saved: {output_file}")

# 4. RFM SEGMENTATION DISTRIBUTION
def plot_rfm_segments():
    csv_path = os.path.join(PROCESSED_DIR, "rfm_segments.csv")
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    # Sort by total revenue
    df_sorted = df.sort_values(by="total_segment_revenue", ascending=True)
    
    y = np.arange(len(df_sorted))
    height = 0.55
    
    colors = ["#94A3B8" if "Lost" in s or "Hibernating" in s else ("#F59E0B" if "Attention" in s or "Risk" in s else "#10B981") for s in df_sorted["customer_segment"]]
    
    bars = ax.barh(y, df_sorted["total_segment_revenue"] / 1000.0, height=height, color=colors, alpha=0.9)
    
    ax.set_yticks(y)
    ax.set_yticklabels(df_sorted["customer_segment"], fontsize=10, weight="bold", color="#1E293B")
    ax.set_xlabel("Total Segment Revenue Contribution ($K)", fontsize=11, weight="bold", color="#334155")
    ax.set_title("Customer RFM Segmentation: Revenue Contribution by Persona", fontsize=13, weight="bold", pad=15, color="#0F172A")
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 12, bar.get_y() + bar.get_height()/2, f"${width:,.0f}K", ha='left', va='center', fontsize=9, color="#1E293B", weight="bold")
        
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    output_file = os.path.join(ASSETS_DIR, "rfm_distribution.png")
    plt.savefig(output_file)
    plt.close()
    print(f"Saved: {output_file}")

if __name__ == "__main__":
    plot_cohort_heatmap()
    plot_monthly_sales_trend()
    plot_retention_decay_curve()
    plot_rfm_segments()
    print("\n[ALL VISUALIZATIONS GENERATED]")
