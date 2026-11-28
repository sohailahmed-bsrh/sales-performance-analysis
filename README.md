# 🛍️ Retail Sales Performance & Revenue Intelligence

An executive commercial analytics and revenue optimization web application built with Python and Streamlit. This project analyzes retail sales transactions across multiple product categories, evaluating customer demographic spend profiles, price sensitivity, and interactive revenue scenario simulations.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Key Features

- **Executive Revenue Cockpit:** Tracks Gross Merchandise Value (GMV), total completed orders, Average Order Value (AOV), and cumulative units sold.
- **Monthly Trajectory & Seasonality:** Temporal analysis revealing seasonal transaction peaks and category demand spikes.
- **Customer Demographic Profiling:** Revenue breakdowns across customer age cohorts (18-25, 26-35, 36-50, 51+) and gender classifications.
- **Basket & Price Elasticity:** Interactive scatter analysis comparing price-per-unit against total transaction value.
- **Interactive Revenue Simulator:** Real-time scenario planner forecasting financial impact from volume growth, pricing shifts, and promotional discounts.

---

## 📊 Analytical Methodology

1. **Transaction Processing:** Ingested 1,000 retail transactions across Beauty, Clothing, and Electronics categories.
2. **Key Insight:** The 26-35 and 36-50 age brackets generate over 58% of gross retail revenue, representing the primary target demographic for targeted marketing campaigns.

---

## 💻 Local Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sohailahmed-bsrh/sales-performance-analysis.git
   cd sales-performance-analysis
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

---

## 🚀 Deployment on Streamlit Community Cloud

1. Fork or push this repository to your GitHub account (`https://github.com/sohailahmed-bsrh/sales-performance-analysis`).
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **New app**.
4. Select repository: `sohailahmed-bsrh/sales-performance-analysis`
5. Branch: `main`
6. Main file path: `app.py`
7. Click **Deploy!**

---

## 👤 Author

**Sohail Ahmed**
- **GitHub:** [@sohailahmed-bsrh](https://github.com/sohailahmed-bsrh)
- **Portfolio:** [https://sohail.devsil.com](https://sohail.devsil.com)
