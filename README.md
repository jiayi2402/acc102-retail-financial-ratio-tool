# Retail Financial Ratio Comparison Tool

## 1. Problem & User
This project builds an interactive Streamlit tool to compare the financial performance of selected listed retail companies. The main analytical problem is:

**How do selected retail companies differ in profitability, liquidity, leverage, and efficiency over time?**

The tool is designed for accounting students, finance beginners, and users who want a simple and interactive way to compare company performance across multiple financial dimensions.

## 2. Data
- **Source:** WRDS
- **Access date:** 2025-04-09
- **Industry:** Retail
- **Candidate companies:** Walmart, Costco, Target, Kroger, Best Buy, Home Depot
- **Time period:** 2020–2024

The project uses annual financial statement data and retains the key raw variables required for ratio calculation, including:
- revenue
- net income
- total assets
- current assets
- current liabilities
- total liabilities
- shareholders’ equity

## 3. Methods
This project uses Python to:
1. extract annual financial statement data from WRDS  
2. clean and prepare the dataset  
3. calculate five key accounting ratios  
4. compare selected companies through tables and charts  
5. build an interactive Streamlit tool for user exploration  

The five ratios used in the project are:
- **ROA**
- **Net Profit Margin**
- **Current Ratio**
- **Debt-to-Equity Ratio**
- **Asset Turnover**

These ratios are used to compare company performance across four dimensions:
- profitability
- liquidity
- leverage
- efficiency

## 4. Key Findings
The analysis shows that the selected retail companies differ clearly across financial dimensions.

- **Home Depot** shows the strongest profitability based on ROA and net profit margin.
- **Costco** shows the strongest asset-use efficiency and appears to be one of the most balanced firms overall.
- **Walmart** appears relatively stable across the selected period.
- **Kroger** generally records weaker profitability and liquidity, but relatively stronger efficiency.
- The results suggest that no single ratio is sufficient to evaluate overall company performance.

Overall, the project shows that a multi-ratio approach provides a more balanced and informative comparison than relying on only one indicator.

## 5. Product Features
The Streamlit tool allows users to:
- select up to three companies
- choose a year range
- choose one or more financial ratios
- view ratio trend charts
- compare the latest-year results
- read automatically generated insight summaries
- view the underlying processed ratio dataset

## 6. Project Files
- `financial_ratio_analysis.ipynb` – Jupyter notebook showing the full analytical workflow
- `app.py` – Streamlit application file
- `cleaned_ratios.csv` – processed dataset used by the app
- `requirements.txt` – required Python packages
- `README.md` – project description and instructions

## 7. How to Run
### Step 1: Install the required packages
`python3 -m pip install -r requirements.txt`

### Step 2: Run the Streamlit app
`python3 -m streamlit run app.py`

### Step 3: Open the local app link
After running the command above, Streamlit will provide a local URL in the terminal, usually something like:
`http://localhost:8501`

## 8. Limitations & Next Steps
This project focuses on a selected group of listed retail companies and a limited set of accounting ratios. Financial ratios are useful summary indicators, but they do not fully capture:
- business strategy
- market conditions
- differences in accounting policy
- management quality
- competitive position

In addition, the project uses annual data, which is suitable for trend comparison but may not fully reflect short-term changes within each year.

Possible future improvements include:
- adding more industries
- including more companies
- adding more financial ratios
- improving the app layout and interactivity
- adding downloadable comparison reports

## 9. Product Link / Demo
- **Tool link:** https://acc102-retail-financial-ratio-tool.streamlit.app
- **Demo video:** [Add your demo video link here]
