# Retail Financial Ratio Comparison Tool

## 1. Problem & User
This project builds an interactive Streamlit tool to compare the financial performance of selected listed retail companies. It is designed for accounting students, finance beginners, and users who want a simple and interactive way to compare profitability, liquidity, leverage, and efficiency across firms over time.

## 2. Data
- **Source:** WRDS
- **Access date:** 15 April 2026
- **Industry:** Retail
- **Final sample companies:** Best Buy, Costco, Dollar General, Dollar Tree, Home Depot, Kroger, Ross Stores, Target, and Walmart
- **Time period:** 2016–2025

The project originally considered a broader pool of listed retail companies. After WRDS extraction and final data screening, the final analytical sample consisted of nine firms with usable annual financial statement data over the selected period.

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

These ratios are used to compare four dimensions of firm performance:
- profitability
- liquidity
- leverage
- efficiency

## 4. Key Findings
- **Home Depot** is the strongest long-run profitability performer based on ROA and net profit margin, making it a useful benchmark for users interested in sustained earnings performance.
- **Ross Stores** appears to be one of the most balanced firms overall, combining strong profitability, strong liquidity, and relatively low leverage, which suggests a more stable overall financial profile.
- **Costco** is the strongest efficiency performer based on asset turnover, indicating particularly effective use of assets to generate sales.
- **Walmart** appears relatively stable across the selected period, which may make it a useful reference point for users comparing consistency rather than extreme performance.
- The results show that no single ratio is sufficient to evaluate overall company performance, so users should compare profitability, liquidity, leverage, and efficiency together rather than rely on only one indicator.

Overall, the project helps users identify whether a firm is stronger in profitability, efficiency, liquidity, or balance-sheet stability, providing a more balanced basis for comparison than relying on a single ratio alone.

## 5. Repository Structure
- `app.py` – Streamlit entry file for the interactive tool
- `cleaned_ratios.csv` – processed dataset used by the app
- `financial_ratio_analysis.ipynb` – notebook showing the full Python workflow
- `requirements.txt` – required Python packages
- `README.md` – project overview and running instructions

## 6. How to Run Locally
The user should be able to run this app locally after cloning or downloading the repository.

Please make sure the following files are in the same project folder:
- `app.py`
- `requirements.txt`
- `cleaned_ratios.csv`

If you use the GitHub web download option, click **Code → Download ZIP**, then extract the ZIP file before running the app.

### macOS
1. Open Terminal and move to the extracted project folder that contains `app.py`  
   Example: `cd ~/Downloads/acc102-retail-financial-ratio-tool-main`

2. Install the required packages  
   `python3 -m pip install -r requirements.txt`

3. Run the Streamlit app  
   `python3 -m streamlit run app.py`

4. Open the local URL shown in the terminal, usually  
   `http://localhost:8501`

### Windows
1. Open Command Prompt or PowerShell and move to the extracted project folder that contains `app.py`  
   Example: `cd path\to\acc102-retail-financial-ratio-tool-main`

2. Install the required packages  
   `python -m pip install -r requirements.txt`

3. Run the Streamlit app  
   `python -m streamlit run app.py`

4. Open the local URL shown in the terminal, usually  
   `http://localhost:8501`

## 7. Repository / Product Link / Demo
- **Project repository link:** https://github.com/jiayi2402/acc102-retail-financial-ratio-tool
- **Optional online demo link:** https://acc102-retail-financial-ratio-tool.streamlit.app
- **Demo video:** [Add your demo video link here]

## 8. Limitations & Next Steps
This project focuses on one industry, a limited sample of firms, and a selected set of accounting ratios. Financial ratios are useful summary indicators, but they do not fully capture business strategy, market conditions, accounting policy differences, management quality, or competitive position.

In addition, some ratios, especially debt-to-equity, require careful interpretation when equity values fluctuate sharply.

Possible future improvements include:
- expanding the company sample
- including more retail sub-segments or additional industries
- adding more financial ratios
- improving the app layout and interactivity
- adding downloadable comparison reports