import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Page configuration
# ---------------------------
st.set_page_config(
    page_title="Retail Financial Ratio Comparison Tool",
    layout="wide"
)

# ---------------------------
# Load data
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_ratios.csv")

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
# Ratio label mapping
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
# Sidebar
# ---------------------------
st.sidebar.header("Select Comparison Options")
st.sidebar.caption("Choose up to three companies for comparison.")

all_companies = sorted(df["company_short"].unique().tolist())

default_companies = ["Best Buy", "Costco", "Home Depot"]
default_companies = [c for c in default_companies if c in all_companies]

selected_companies = st.sidebar.multiselect(
    "Companies",
    options=all_companies,
    default=default_companies
)

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
# Main title and introduction
# ---------------------------
st.title("Retail Financial Ratio Comparison Tool")
st.write(
    """
    This interactive tool compares the financial performance of a final sample of nine listed retail companies
    over the 2016–2025 period. It helps users explore profitability, liquidity, leverage, and efficiency
    through ratio trends, latest-year comparison, and summary insights.
    """
)

# ---------------------------
# How to use
# ---------------------------
st.subheader("How to Use This Tool")
st.write(
    """
    Select up to three companies from the sidebar, choose a year range, and select one or more financial ratios.
    The trend charts show how each ratio changes over time, while the latest-year comparison table and insight summary
    help users interpret the most recent results more quickly.
    """
)

# ---------------------------
# Data scope
# ---------------------------
st.subheader("Data Scope")
st.write(
    """
    The tool uses annual financial statement data from WRDS for a final sample of nine listed retail companies
    over the 2016–2025 period.
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
# Validation checks
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
    st.warning("No data are available for the selected companies and year range.")
    st.stop()

# ---------------------------
# Ratio trends
# ---------------------------
st.subheader("Ratio Trends Over Time")
st.write(
    "These charts help users compare how each selected ratio changes over time across the chosen companies."
)

years = sorted(filtered["fiscal_year"].unique())

for ratio in selected_ratios:
    fig, ax = plt.subplots(figsize=(8, 5))

    for company in filtered["company_short"].unique():
        temp = filtered[filtered["company_short"] == company]
        ax.plot(temp["fiscal_year"], temp[ratio], marker="o", label=company)

    ax.set_xticks(years)
    ax.set_xticklabels([str(int(y)) for y in years])
    ax.set_title(f"{ratio_name_map[ratio]} Trend")
    ax.set_xlabel("Fiscal Year")
    ax.set_ylabel(ratio_name_map[ratio])
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
    plt.close(fig)

# ---------------------------
# Latest-year comparison
# ---------------------------
st.subheader("Latest-Year Comparison")

latest_year = int(filtered["fiscal_year"].max())
latest_df = filtered[filtered["fiscal_year"] == latest_year].copy()

st.write(
    f"This table compares the selected companies in the most recent year within the chosen range: **{latest_year}**."
)

latest_cols = ["company_short"] + selected_ratios
latest_comparison = latest_df[latest_cols].copy()
latest_comparison = latest_comparison.rename(columns={"company_short": "Company"})
latest_comparison[selected_ratios] = latest_comparison[selected_ratios].round(4)

# Rename ratio columns for display
latest_comparison = latest_comparison.rename(columns=ratio_name_map)

st.dataframe(latest_comparison, use_container_width=True)

# ---------------------------
# Insight summary
# ---------------------------
st.subheader("Insight Summary")
st.write(
    "The summary below highlights the strongest observations in the selected view and gives a brief interpretation of what they may imply."
)

summary_points = []

if "roa" in selected_ratios:
    top_roa = latest_df.loc[latest_df["roa"].idxmax()]
    summary_points.append(
        f"**{top_roa['company_short']}** has the highest ROA in {latest_year}, suggesting relatively strong profitability in relation to total assets."
    )

if "net_profit_margin" in selected_ratios:
    top_npm = latest_df.loc[latest_df["net_profit_margin"].idxmax()]
    summary_points.append(
        f"**{top_npm['company_short']}** has the highest net profit margin in {latest_year}, indicating relatively strong earnings performance relative to sales."
    )

if "current_ratio" in selected_ratios:
    top_cr = latest_df.loc[latest_df["current_ratio"].idxmax()]
    summary_points.append(
        f"**{top_cr['company_short']}** shows the strongest current ratio in {latest_year}, indicating a relatively stronger short-term liquidity position."
    )

if "debt_to_equity" in selected_ratios:
    low_de = latest_df.loc[latest_df["debt_to_equity"].idxmin()]
    high_de = latest_df.loc[latest_df["debt_to_equity"].idxmax()]

    summary_points.append(
        f"**{low_de['company_short']}** has the lowest debt-to-equity ratio in {latest_year}, suggesting relatively lower leverage than the other selected firms."
    )

    if len(latest_df) > 1:
        summary_points.append(
            f"**{high_de['company_short']}** has the highest debt-to-equity ratio in {latest_year}, which may indicate heavier reliance on leveraged financing and should be interpreted with caution."
        )

if "asset_turnover" in selected_ratios:
    top_at = latest_df.loc[latest_df["asset_turnover"].idxmax()]
    summary_points.append(
        f"**{top_at['company_short']}** shows the highest asset turnover in {latest_year}, suggesting relatively strong efficiency in using assets to generate sales."
    )

if len(selected_ratios) >= 2:
    summary_points.append(
        "These results should be interpreted jointly, because a company that performs strongly in one ratio may appear weaker in another."
    )

for point in summary_points:
    st.markdown(f"- {point}")

# ---------------------------
# Underlying ratio data
# ---------------------------
st.subheader("Underlying Ratio Data")
st.write(
    "The table below shows the processed ratio data behind the current selection."
)

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
display_df = display_df.rename(columns={"company_short": "Company", "fiscal_year": "Fiscal Year"})
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

display_df = display_df.rename(columns=ratio_name_map)

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
    fluctuate sharply. The tool is intended to support comparison and interpretation rather than provide a complete measure
    of overall company performance.
    """
)

st.write(
    "This tool is intended for educational comparison and interpretation rather than investment or professional advisory use."
)