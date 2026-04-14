# Retail Financial Ratio Comparison Tool

## 1. Problem & User
This project builds an interactive Streamlit tool to compare the financial performance of selected listed retail companies. It is designed for accounting students, finance beginners, and users who want a simple way to compare profitability, liquidity, leverage, and efficiency across firms over time.

## 2. Data
- **Source:** WRDS
- **Access date:** 2026-04-14
- **Industry:** Retail
- **Final sample companies:** Best Buy, Costco, Dollar General, Dollar Tree, Home Depot, Kroger, Ross Stores, Target, and Walmart
- **Time period:** 2016–2025

The project uses annual financial statement data and retains the key variables required for ratio calculation, including:
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
4. generate summary tables and visual comparisons  
5. build an interactive Streamlit tool for user exploration  

The five ratios used are:
- ROA
- Net Profit Margin
- Current Ratio
- Debt-to-Equity Ratio
- Asset Turnover

## 4. Key Findings
- **Home Depot** is the strongest long-run profitability performer based on ROA and net profit margin.
- **Ross Stores** appears to be one of the most balanced firms overall, combining strong profitability, strong liquidity, and relatively low leverage.
- **Costco** is the strongest efficiency performer based on asset turnover.
- **Walmart** appears relatively stable across the selected period.
- The results show that no single ratio is sufficient to evaluate overall company performance.

## 5. How to Run
1. Install the required packages:  
   `python3 -m pip install -r requirements.txt`

2. Run the Streamlit app:  
   `python3 -m streamlit run app.py`

3. Open the local app link provided in the terminal, usually:  
   `http://localhost:8501`

## 6. Product Link / Demo
- **Tool link:** https://acc102-retail-financial-ratio-tool.streamlit.app
- **Demo video:** [Add your demo video link here]

## 7. Limitations & Next Steps
This project focuses on one industry, a limited sample of firms, and a selected set of accounting ratios. Financial ratios are useful summary indicators, but they do not fully capture business strategy, market conditions, accounting policy differences, or management quality.

Possible future improvements include:
- expanding the company sample
- including more retail sub-segments or additional industries
- adding more financial ratios
- improving the app layout and interactivity
- adding downloadable comparison reports