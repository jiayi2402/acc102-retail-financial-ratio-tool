import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Financial Ratio Comparison Tool", layout="wide")

# ---------------------------
# Load data
# ---------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_ratios.csv")
    return df

df = load_data()

# ---------------------------
# Company name mapping
# ---------------------------
name_map = {
    "BEST BUY CO INC": "Best Buy",
    "COSTCO WHOLESALE CORP": "Costco",
    "DOLLAR GENERAL CORP": "Dollar General",
    "DOLLAR TREE INC": "Dollar Tree",
    "HOME DEPOT INC": "Home Depot",
    "KROGER CO": "Kroger",
    "ROSS STORES INC": "Ross Stores",
    "TARGET CORP": "Target",
    "WALMART INC": "Walmart"
}

df["company_short"] = df["company"].map(name_map).fillna(df["company"])

# ---------------------------
# Ratio display names
# ---------------------------
ratio_name_map = {
    "roa": "ROA",
    "net_profit_margin": "Net Profit Margin",
    "current_ratio": "Current Ratio",
    "debt_to_equity": "Debt-to-Equity Ratio",
    "asset_turnover": "Asset Turnover"
}

ratio_options = list(ratio_name_map.keys())

# ---------------------------
# Sidebar controls
# ---------------------------
st.sidebar.header("Select Comparison Options")
st.sidebar.write("Choose up to three companies")

all_companies = sorted(df["company_short"].unique().tolist())

default_companies = ["Best Buy", "Costco", "Dollar General"]
default_companies = [c for c in default_companies if c in all_companies]

selected_companies = st.sidebar.multiselect(
    "Companies",
    options=all_companies,
    default=default_companies
)

if len(selected_companies) > 3:
    st.sidebar.warning("Please select up to three companies only.")

min_year = int(df["fiscal_year"].min())
max_year = int(df["fiscal_year"].max())

selected_years = st.sidebar.slider(
    "Select year range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

selected_ratios = st.sidebar.multiselect(
    "Select financial ratios",
    options=ratio_options,
    default=ratio_options
)

# ---------------------------
# Filter data
# ---------------------------
filtered = df[
    (df["company_short"].isin(selected_companies)) &
    (df["fiscal_year"] >= selected_years[0]) &
    (df["fiscal_year"] <= selected_years[1])
].copy()

# ---------------------------
# Main title and intro
# ---------------------------
st.title("Retail Financial Ratio Comparison Tool")
st.write(
    """
    This interactive tool compares the financial performance of a final sample of nine listed retail companies
    over the 2016–2025 period. It is designed to help users explore profitability, liquidity, leverage,
    and efficiency through ratio trends, latest-year comparison, and summary insights.
    """
)

# ---------------------------
# Project overview
# ---------------------------
st.subheader("Project Overview")
st.write(f"**Selected companies:** {', '.join(selected_companies) if selected_companies else 'None selected'}")
st.write(f"**Selected years:** {selected_years[0]} to {selected_years[1]}")
st.write(
    f"**Selected ratios:** "
    f"{', '.join([ratio_name_map[r] for r in selected_ratios]) if selected_ratios else 'None selected'}"
)

# ---------------------------
# Guard clauses
# ---------------------------
if len(selected_companies) == 0:
    st.warning("Please select at least one company.")
    st.stop()

if len(selected_companies) > 3:
    st.warning("Please reduce the company selection to three or fewer.")
    st.stop()

if len(selected_ratios) == 0:
    st.warning("Please select at least one financial ratio.")
    st.stop()

if filtered.empty:
    st.warning("No data available for the selected companies and year range.")
    st.stop()

# ---------------------------
# Trend charts
# ---------------------------
st.subheader("Ratio Trends Over Time")

years = sorted(filtered["fiscal_year"].unique())

for ratio in selected_ratios:
    plt.figure(figsize=(8, 5))

    for company in filtered["company_short"].unique():
        temp = filtered[filtered["company_short"] == company]
        plt.plot(temp["fiscal_year"], temp[ratio], marker="o", label=company)

    plt.gca().set_xticks(years)
    plt.gca().set_xticklabels([str(int(y)) for y in years])

    plt.title(f"{ratio_name_map[ratio]} Trend")
    plt.xlabel("Fiscal Year")
    plt.ylabel(ratio_name_map[ratio])
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    plt.close()

# ---------------------------
# Latest-year comparison
# ---------------------------
st.subheader("Latest-Year Comparison")

latest_year = int(filtered["fiscal_year"].max())
latest_df = filtered[filtered["fiscal_year"] == latest_year].copy()

st.write(f"Comparison for the latest year in the selected range: **{latest_year}**")

latest_cols = ["company_short"] + selected_ratios
latest_comparison = latest_df[latest_cols].copy()
latest_comparison = latest_comparison.rename(columns={"company_short": "Company"})
latest_comparison[selected_ratios] = latest_comparison[selected_ratios].round(4)

st.dataframe(latest_comparison, use_container_width=True)

# ---------------------------
# Insight summary
# ---------------------------
st.subheader("Insight Summary")

summary_points = []

# Profitability
if "roa" in selected_ratios:
    top_roa = latest_df.loc[latest_df["roa"].idxmax()]
    summary_points.append(
        f"**{top_roa['company_short']}** has the highest ROA in {latest_year}."
    )

if "net_profit_margin" in selected_ratios:
    top_npm = latest_df.loc[latest_df["net_profit_margin"].idxmax()]
    summary_points.append(
        f"**{top_npm['company_short']}** has the highest net profit margin in {latest_year}."
    )

# Liquidity
if "current_ratio" in selected_ratios:
    top_cr = latest_df.loc[latest_df["current_ratio"].idxmax()]
    summary_points.append(
        f"**{top_cr['company_short']}** shows the strongest current ratio in {latest_year}."
    )

# Leverage
if "debt_to_equity" in selected_ratios:
    low_de = latest_df.loc[latest_df["debt_to_equity"].idxmin()]
    summary_points.append(
        f"**{low_de['company_short']}** has the lowest debt-to-equity ratio in {latest_year}, suggesting relatively lower leverage."
    )

# Efficiency
if "asset_turnover" in selected_ratios:
    top_at = latest_df.loc[latest_df["asset_turnover"].idxmax()]
    summary_points.append(
        f"**{top_at['company_short']}** shows the highest asset turnover in {latest_year}."
    )

if summary_points:
    for point in summary_points:
        st.markdown(f"- {point}")

# ---------------------------
# Underlying ratio data
# ---------------------------
st.subheader("Underlying Ratio Data")

display_cols = [
    "company_short",
    "fiscal_year",
    "roa",
    "net_profit_margin",
    "current_ratio",
    "debt_to_equity",
    "asset_turnover"
]

display_df = filtered[display_cols].copy()
display_df = display_df.rename(columns={"company_short": "Company"})
display_df[[
    "roa",
    "net_profit_margin",
    "current_ratio",
    "debt_to_equity",
    "asset_turnover"
]] = display_df[[
    "roa",
    "net_profit_margin",
    "current_ratio",
    "debt_to_equity",
    "asset_turnover"
]].round(4)

st.dataframe(display_df, use_container_width=True)

# ---------------------------
# Notes and limitations
# ---------------------------
st.subheader("Notes and Limitations")
st.write(
    """
    This tool compares a final sample of nine listed retail companies using annual accounting ratios over the 2016–2025 period.
    The results should be interpreted with caution, because financial ratios do not fully capture business strategy,
    market conditions, competitive position, management quality, or differences in accounting policy.
    In addition, some ratios, especially the debt-to-equity ratio, may become difficult to interpret when equity values
    fluctuate sharply. The tool is therefore intended to support comparison and interpretation, rather than provide a
    complete measure of overall company performance.
    """
)