import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Retail Financial Ratio Comparison Tool",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("cleaned_ratios.csv")

# -----------------------------
# Company name mapping
# -----------------------------
name_map = {
    "BEST BUY CO INC": "Best Buy",
    "COSTCO WHOLESALE CORP": "Costco",
    "HOME DEPOT INC": "Home Depot",
    "KROGER CO": "Kroger",
    "TARGET CORP": "Target",
    "WALMART INC": "Walmart"
}

df["company_short"] = df["company"].map(name_map)

# If any company is not in the mapping, keep the original name
df["company_short"] = df["company_short"].fillna(df["company"])

# -----------------------------
# Title and introduction
# -----------------------------
st.title("Retail Financial Ratio Comparison Tool")
st.write(
    """
    This interactive tool compares selected listed retail companies using key accounting ratios.
    It helps users examine profitability, liquidity, leverage, and efficiency across different firms and over time.
    """
)

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("Select Comparison Options")

all_companies = sorted(df["company_short"].unique())
all_years = sorted(df["fiscal_year"].unique())

all_ratios = {
    "ROA": "roa",
    "Net Profit Margin": "net_profit_margin",
    "Current Ratio": "current_ratio",
    "Debt-to-Equity Ratio": "debt_to_equity",
    "Asset Turnover": "asset_turnover"
}

selected_companies = st.sidebar.multiselect(
    "Choose up to three companies",
    options=all_companies,
    default=all_companies[:3]
)

selected_years = st.sidebar.slider(
    "Select year range",
    min_value=min(all_years),
    max_value=max(all_years),
    value=(min(all_years), max(all_years))
)

selected_ratio_names = st.sidebar.multiselect(
    "Select financial ratios",
    options=list(all_ratios.keys()),
    default=list(all_ratios.keys())
)

# -----------------------------
# Input validation
# -----------------------------
if len(selected_companies) == 0:
    st.warning("Please select at least one company.")
    st.stop()

if len(selected_companies) > 3:
    st.warning("Please select no more than three companies.")
    st.stop()

if len(selected_ratio_names) == 0:
    st.warning("Please select at least one financial ratio.")
    st.stop()

# -----------------------------
# Filter data
# -----------------------------
filtered_df = df[
    (df["company_short"].isin(selected_companies)) &
    (df["fiscal_year"] >= selected_years[0]) &
    (df["fiscal_year"] <= selected_years[1])
].copy()

if filtered_df.empty:
    st.warning("No data available for the selected options.")
    st.stop()

# -----------------------------
# Project overview
# -----------------------------
st.subheader("Project Overview")
st.write(f"**Selected companies:** {', '.join(selected_companies)}")
st.write(f"**Selected years:** {selected_years[0]} to {selected_years[1]}")
st.write(f"**Selected ratios:** {', '.join(selected_ratio_names)}")

# -----------------------------
# Ratio trends
# -----------------------------
st.subheader("Ratio Trends Over Time")

for ratio_name in selected_ratio_names:
    ratio_col = all_ratios[ratio_name]

    fig, ax = plt.subplots(figsize=(8, 4))

    for company in selected_companies:
        temp = filtered_df[filtered_df["company_short"] == company]
        ax.plot(
            temp["fiscal_year"],
            temp[ratio_col],
            marker="o",
            label=company
        )

    ax.set_title(f"{ratio_name} Trend")
    ax.set_xlabel("Fiscal Year")
    ax.set_ylabel(ratio_name)
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

# -----------------------------
# Latest-year comparison
# -----------------------------
st.subheader("Latest-Year Comparison")

latest_year = filtered_df["fiscal_year"].max()
latest_df = filtered_df[filtered_df["fiscal_year"] == latest_year].copy()

st.write(f"Comparison for the latest year in the selected range: **{latest_year}**")

latest_table = latest_df[["company_short"] + [all_ratios[name] for name in selected_ratio_names]].copy()
latest_table = latest_table.rename(columns={"company_short": "Company"})
st.dataframe(latest_table, use_container_width=True)

# -----------------------------
# Insight summary
# -----------------------------
st.subheader("Insight Summary")

insights = []

if "ROA" in selected_ratio_names:
    best_roa_company = latest_df.loc[latest_df["roa"].idxmax(), "company_short"]
    insights.append(f"**{best_roa_company}** has the highest ROA in {latest_year}.")

if "Net Profit Margin" in selected_ratio_names:
    best_margin_company = latest_df.loc[latest_df["net_profit_margin"].idxmax(), "company_short"]
    insights.append(f"**{best_margin_company}** has the highest net profit margin in {latest_year}.")

if "Current Ratio" in selected_ratio_names:
    best_current_company = latest_df.loc[latest_df["current_ratio"].idxmax(), "company_short"]
    insights.append(f"**{best_current_company}** shows the strongest current ratio in {latest_year}.")

if "Debt-to-Equity Ratio" in selected_ratio_names:
    lowest_de_company = latest_df.loc[latest_df["debt_to_equity"].idxmin(), "company_short"]
    insights.append(f"**{lowest_de_company}** has the lowest debt-to-equity ratio in {latest_year}, suggesting relatively lower leverage.")

if "Asset Turnover" in selected_ratio_names:
    best_turnover_company = latest_df.loc[latest_df["asset_turnover"].idxmax(), "company_short"]
    insights.append(f"**{best_turnover_company}** shows the highest asset turnover in {latest_year}.")

for insight in insights:
    st.write(f"- {insight}")

# -----------------------------
# Underlying ratio data
# -----------------------------
st.subheader("Underlying Ratio Data")

display_df = filtered_df[[
    "company_short",
    "fiscal_year",
    "roa",
    "net_profit_margin",
    "current_ratio",
    "debt_to_equity",
    "asset_turnover"
]].copy()

display_df = display_df.rename(columns={
    "company_short": "Company",
    "fiscal_year": "Fiscal Year",
    "roa": "ROA",
    "net_profit_margin": "Net Profit Margin",
    "current_ratio": "Current Ratio",
    "debt_to_equity": "Debt-to-Equity Ratio",
    "asset_turnover": "Asset Turnover"
})

st.dataframe(display_df, use_container_width=True)

# -----------------------------
# Notes and limitations
# -----------------------------
st.subheader("Notes and Limitations")
st.write(
    """
    This tool compares a selected group of retail companies using annual accounting ratios.
    The results should be interpreted with caution, since financial ratios do not capture all business differences,
    strategic choices, or accounting policy variations.
    """
)