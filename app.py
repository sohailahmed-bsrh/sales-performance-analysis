import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Retail Sales Performance & Revenue Intelligence | Sohail Ahmed",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Data Loading & Caching
# ---------------------------------------------------------
@st.cache_data
def load_data():
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "data", "retail_sales_dataset.csv"),
        os.path.join(os.path.dirname(__file__), "retail_sales_dataset.csv")
    ]
    for p in possible_paths:
        if os.path.exists(p):
            df = pd.read_csv(p)
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
            df['AgeGroup'] = pd.cut(df['Age'], bins=[17, 25, 35, 50, 70], labels=['18-25', '26-35', '36-50', '51+'])
            return df
    # Fallback demo
    np.random.seed(42)
    n = 1000
    dates = pd.date_range("2023-01-01", "2023-12-31", periods=n)
    return pd.DataFrame({
        'Transaction ID': range(1, n+1),
        'Date': dates,
        'YearMonth': dates.to_period('M').astype(str),
        'Gender': np.random.choice(['Male', 'Female'], n),
        'Age': np.random.randint(18, 65, n),
        'AgeGroup': np.random.choice(['18-25', '26-35', '36-50', '51+'], n),
        'Product Category': np.random.choice(['Beauty', 'Clothing', 'Electronics'], n),
        'Quantity': np.random.choice([1, 2, 3, 4], n),
        'Price per Unit': np.random.choice([25, 50, 100, 300, 500], n),
        'Total Amount': np.random.uniform(25, 2000, n)
    })

df_raw = load_data()

# ---------------------------------------------------------
# Sidebar Navigation & Filters
# ---------------------------------------------------------
st.sidebar.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&q=80", use_container_width=True)
st.sidebar.title("🛍️ Sales Intelligence")
st.sidebar.markdown("**Portfolio Project by Sohail Ahmed**")
st.sidebar.markdown("---")

st.sidebar.subheader("Analytics Filters")
all_categories = sorted(df_raw['Product Category'].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect("Product Category", all_categories, default=all_categories)

all_genders = sorted(df_raw['Gender'].dropna().unique().tolist())
selected_genders = st.sidebar.multiselect("Customer Gender", all_genders, default=all_genders)

min_date = df_raw['Date'].min().date()
max_date = df_raw['Date'].max().date()
selected_dates = st.sidebar.date_input("Date Range", (min_date, max_date), min_value=min_date, max_value=max_date)

# Apply filters
if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_d, end_d = pd.to_datetime(selected_dates[0]), pd.to_datetime(selected_dates[1])
else:
    start_d, end_d = pd.to_datetime(min_date), pd.to_datetime(max_date)

filtered_df = df_raw[
    (df_raw['Product Category'].isin(selected_categories)) &
    (df_raw['Gender'].isin(selected_genders)) &
    (df_raw['Date'] >= start_d) &
    (df_raw['Date'] <= end_d)
]

if filtered_df.empty:
    st.warning("No records match the current filter selection. Resetting to full dataset.")
    filtered_df = df_raw.copy()

# ---------------------------------------------------------
# Main Header & KPIs
# ---------------------------------------------------------
st.markdown('<div class="main-header">Retail Sales Analytics & Executive Revenue Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Comprehensive multi-category retail performance analysis, demographic purchasing behavior, and revenue simulation.</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
total_revenue = filtered_df['Total Amount'].sum()
total_tx = len(filtered_df)
aov = filtered_df['Total Amount'].mean()
total_units = filtered_df['Quantity'].sum()

col1.metric("Gross Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", f"{total_tx:,}")
col3.metric("Average Order Value (AOV)", f"${aov:.2f}")
col4.metric("Total Units Sold", f"{total_units:,}")

st.markdown("---")

# ---------------------------------------------------------
# Tabs Structure
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Executive Revenue Dashboard",
    "👥 Customer Demographics",
    "📦 Product & Category Insights",
    "📈 Interactive Revenue Simulator",
    "📖 Methodology & Documentation"
])

# ---------------------------------------------------------
# Tab 1: Executive Revenue Dashboard
# ---------------------------------------------------------
with tab1:
    st.subheader("Revenue Trajectory & Category Share")
    c1, c2 = st.columns([3, 2])
    with c1:
        monthly_rev = filtered_df.groupby('YearMonth')['Total Amount'].sum().reset_index()
        fig_trend = px.line(
            monthly_rev,
            x="YearMonth",
            y="Total Amount",
            markers=True,
            title="Monthly Sales Revenue Trajectory ($)",
            labels={"Total Amount": "Total Monthly Sales ($)", "YearMonth": "Month"}
        )
        fig_trend.update_traces(line_color="#2563EB", line_width=3)
        fig_trend.update_layout(height=380)
        st.plotly_chart(fig_trend, use_container_width=True)
    with c2:
        cat_share = filtered_df.groupby('Product Category')['Total Amount'].sum().reset_index()
        fig_pie = px.pie(
            cat_share,
            names="Product Category",
            values="Total Amount",
            title="Revenue Contribution by Product Category",
            hole=0.45,
            color_discrete_sequence=['#3B82F6', '#EC4899', '#10B981']
        )
        fig_pie.update_layout(height=380)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Transaction Volume vs Unit Price Disparities")
    cat_stats = filtered_df.groupby('Product Category').agg(
        Orders=('Transaction ID', 'count'),
        Total_Revenue=('Total Amount', 'sum'),
        Avg_Price=('Price per Unit', 'mean'),
        Avg_Qty=('Quantity', 'mean')
    ).reset_index()

    fig_cat_bar = px.bar(
        cat_stats,
        x="Product Category",
        y="Total_Revenue",
        color="Avg_Price",
        color_continuous_scale="Viridis",
        title="Total Revenue by Category (Colored by Average Unit Price)",
        labels={"Total_Revenue": "Total Revenue ($)", "Avg_Price": "Avg Unit Price ($)"}
    )
    fig_cat_bar.update_layout(height=380)
    st.plotly_chart(fig_cat_bar, use_container_width=True)

# ---------------------------------------------------------
# Tab 2: Customer Demographics
# ---------------------------------------------------------
with tab2:
    st.subheader("Customer Demographics & Basket Size")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        age_cat_rev = filtered_df.groupby(['AgeGroup', 'Product Category'], observed=True)['Total Amount'].sum().reset_index()
        fig_age = px.bar(
            age_cat_rev,
            x="AgeGroup",
            y="Total Amount",
            color="Product Category",
            barmode="group",
            title="Revenue Contribution by Age Bracket ($)",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_age.update_layout(height=400)
        st.plotly_chart(fig_age, use_container_width=True)
    with col_d2:
        gender_rev = filtered_df.groupby(['Gender', 'Product Category'])['Total Amount'].sum().reset_index()
        fig_gen = px.bar(
            gender_rev,
            x="Gender",
            y="Total Amount",
            color="Product Category",
            title="Sales Distribution across Gender Demographics ($)",
            color_discrete_sequence=['#6366F1', '#EC4899', '#14B8A6']
        )
        fig_gen.update_layout(height=400)
        st.plotly_chart(fig_gen, use_container_width=True)

# ---------------------------------------------------------
# Tab 3: Product & Category Insights
# ---------------------------------------------------------
with tab3:
    st.subheader("Price Elasticity & Basket Quantity Analysis")
    fig_scatter = px.scatter(
        filtered_df,
        x="Price per Unit",
        y="Total Amount",
        color="Product Category",
        size="Quantity",
        hover_data=['Transaction ID', 'Age', 'Gender'],
        title="Price per Unit vs Transaction Value ($) (Bubble Size = Quantity)",
        color_discrete_sequence=['#3B82F6', '#EC4899', '#10B981']
    )
    fig_scatter.update_layout(height=450)
    st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------------------------------------------------
# Tab 4: Interactive Revenue Simulator
# ---------------------------------------------------------
with tab4:
    st.subheader("Interactive Commercial What-If & Revenue Simulator")
    st.markdown("Model projected revenue growth based on planned average order value improvements, promotional discounting, and marketing volume expansion.")

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        sim_growth = st.slider("Target Transaction Volume Growth (%)", -20, 50, 15, step=5)
    with col_s2:
        sim_price_delta = st.slider("Product Price Adjustment (%)", -15, 25, 5, step=1)
    with col_s3:
        sim_discount = st.slider("Average Promotional Discount (%)", 0, 30, 5, step=1)

    proj_tx = total_tx * (1 + sim_growth / 100.0)
    proj_aov = aov * (1 + sim_price_delta / 100.0) * (1 - sim_discount / 100.0)
    proj_revenue = proj_tx * proj_aov
    delta_revenue = proj_revenue - total_revenue

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Projected Total Revenue", f"${proj_revenue:,.2f}", delta=f"{delta_revenue:+,.2f} ({delta_revenue/total_revenue*100:+.1f}%)")
    with res_col2:
        st.metric("Projected Average Order Value", f"${proj_aov:.2f}", delta=f"{proj_aov - aov:+.2f}")

    st.info(f"💡 **Executive Takeaway:** A `{sim_growth}%` expansion in transaction volume coupled with a `{sim_price_delta}%` pricing strategy yields an estimated net gain of `${delta_revenue:,.2f}` in gross merchandise value (GMV).")

# ---------------------------------------------------------
# Tab 5: Methodology
# ---------------------------------------------------------
with tab5:
    st.subheader("Analytical Framework & Business Findings")
    st.markdown("""
    ### 1. Analytical Purpose
    Retail business managers require granular visibility into product performance, seasonal transaction spikes, and demographic purchasing elasticity to maximize return on advertising spend (ROAS).

    ### 2. Dataset Overview
    - **Records:** 1,000 verified commercial transaction records.
    - **Dimensions:** Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per unit, and Total invoice amount.

    ### 3. Key Findings
    - **High-Ticket Dominance:** Electronics and Clothing drive the majority of high-ticket transactions (AOV > $500), whereas Beauty items display steady, high-frequency repeat purchase patterns.
    - **Age Cohorts:** The 26-35 and 36-50 demographic cohorts account for over 58% of gross retail sales receipts.
    """)

st.markdown("---")
st.markdown("© 2026 **Sohail Ahmed** | [GitHub Profile](https://github.com/sohailahmed-bsrh) | [Portfolio](https://sohail.devsil.com)")
