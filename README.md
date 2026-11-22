# Sales Performance & Revenue Intelligence Analytics Engine

<p align="center">
  <a href="https://sohail.devsil.com"><strong>Portfolio</strong></a> | 
  <a href="https://github.com/sohailahmed-bsrh"><strong>GitHub Profile</strong></a> | 
  <a href="https://github.com/sohailahmed-bsrh/sales-performance-analysis"><strong>Source Repository</strong></a>
</p>

---

## Executive Summary & Problem Statement

Modern enterprise sales operations generate massive transactional data streams across geographical regions, product categories, and sales channels. Without structured statistical analysis and cohort segmentation, leadership teams operate on surface-level averages, masking underperforming regions, margin compression, and customer churn.

This repository provides an enterprise-grade **Sales Performance Analytics and Revenue Intelligence Suite**. Applying statistical hypothesis testing, RFM (Recency, Frequency, Monetary) customer segmentation, and cohort lifetime value modeling, it extracts actionable drivers of revenue growth and profitability.

<div align="center">
  <img src="https://raw.githubusercontent.com/sohailahmed-bsrh/myportfolio/main/assets/images/thumbnail/sales-data-analysis.jpeg" width="650" alt="Sales Performance Analysis Engine"/>
  <p><em>Enterprise revenue analytics, multi-channel cohort modeling, and RFM customer value segmentation.</em></p>
</div>

---

## Real-World Industry Applications

- **Executive Revenue Forecasting**: Tracks Monthly Recurring Revenue (MRR), Annual Recurring Revenue (ARR), and Year-over-Year (YoY) trajectory.
- **RFM Customer Segmentation**: Categorizes customer bases into Champions, Potential Loyalists, At-Risk, and Dormant tiers.
- **Product Portfolio Rationalization**: Uncovers profit margin distributions and isolates high-volume, low-margin margin-diluting SKUs.
- **Regional Sales Territory Planning**: Optimizes sales quotas and commission incentives by benchmarking territory conversion rates.

---

## Technical Architecture & Engineering Walkthrough

```
                      [Multi-Year Transactional Sales Ledger]
                                         │
                                         ▼
                     [Data Integrity & Normalization Pipeline]
                  (Datetime Indexing, Refund Deduplication, Currency)
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
[Cohort Retention Matrix]      [RFM Segmentation Engine]       [Pareto Profitability]
(Month-by-Month Decay)         (Quantile Scoring Tiers)        (80/20 SKU Analysis)
         │                               │                               │
         └───────────────────────────────┼───────────────────────────────┘
                                         │
                                         ▼
                     [Interactive Executive Analytics Reports]
```

### Step 1: Ledger Ingestion & Data Sanitization
Cleans raw transaction logs (`notebooks/sales_dataset_analysis.ipynb`), resolving invoice duplicates, handling returns/cancellations, parsing international date formats, and computing net realized revenue.

### Step 2: Temporal Decomposition & Seasonality Analysis
Decomposes revenue streams into trend, seasonal, and cyclical variations to isolate true underlying growth from quarterly promotions and holiday spikes.

### Step 3: RFM Value Segmentation
Calculates Recency (days since last purchase), Frequency (total transaction count), and Monetary value (total spend) per customer. Assigns quantile scores $(1-5)$ to establish actionable behavioral customer segments.

### Step 4: Cohort Retention & Lifetime Value Analysis
Groups customers into acquisition cohorts to monitor month-over-month retention decay curves and calculate average Customer Lifetime Value (CLV).

### Step 5: Pareto Product Optimization
Applies the 80/20 Pareto principle to SKU catalogs, categorizing products into high-impact revenue drivers vs inventory cost burdens.

---

## Technology Stack & Implementation Specifications

| Component | Technology | Version | Architectural Function |
| :--- | :--- | :--- | :--- |
| **Analytics Engine** | Python / Pandas | 2.x | High-performance multi-index transactional aggregation |
| **Numerical Processing** | NumPy / SciPy | Latest | Statistical distribution testing and quantile scoring |
| **Data Visualization** | Seaborn / Matplotlib | 3.8+ | Heatmaps, cohort retention matrices, pareto charts |
| **Statistical Modeling** | Statsmodels | 0.14+ | Time-series trend and seasonal regression modeling |

---

## Installation & Execution Guide

```bash
git clone https://github.com/sohailahmed-bsrh/sales-performance-analysis.git
cd sales-performance-analysis
python -m venv venv
# Windows: venv\Scriptsctivate | Unix: source venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/sales_dataset_analysis.ipynb
```

---

## Author & Contact Information

<table width="100%">
  <tr>
    <td width="150" align="center" valign="middle">
      <img src="https://avatars.githubusercontent.com/u/231165170?v=4" width="120" style="border-radius: 50%;" alt="Sohail Ahmed"/>
    </td>
    <td>
      <h3>Sohail Ahmed</h3>
      <p><strong>Senior Software Engineer & AI Systems Architect</strong></p>
      <p>Specializing in Full-Stack AI Application Development, Computer Vision, Deep Learning Pipelines, and Scalable Automation Architectures.</p>
      <p>
        <a href="https://sohail.devsil.com"><strong>Portfolio Website</strong></a> | 
        <a href="https://github.com/sohailahmed-bsrh"><strong>GitHub Profile</strong></a> | 
        <a href="https://www.linkedin.com/in/sohail-ahmed-546314316/"><strong>LinkedIn</strong></a> | 
        <a href="mailto:se906403@gmail.com"><strong>Email Contact</strong></a>
      </p>
    </td>
  </tr>
</table>
