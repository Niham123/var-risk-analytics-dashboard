# 🛡️ Quantitative Risk & VaR Analytics Dashboard

An interactive quantitative risk management dashboard built in Python using **Streamlit**, **yFinance**, and **SciPy**. This application calculates key portfolio risk metrics—including Parametric Value at Risk (VaR), Historical VaR, and Conditional VaR (Expected Shortfall)—for multi-asset portfolios.

🚀 **Live Interactive Demo:** [Launch Dashboard on Streamlit Cloud](https://var-risk-analytics-dashboard-adqxxwrtm9epnzximyvupa.streamlit.app)


---

## 📌 Key Features

* **Real-Time Data Ingestion:** Fetches multi-year historical daily adjusted closing prices via Yahoo Finance (`yfinance`).
* **Parametric VaR & CVaR:** Parametric normal distribution modeling using cumulative distribution functions (`scipy.stats.norm`).
* **Historical Simulation VaR & CVaR:** Non-parametric empirical distribution cutoff and tail-loss analytics.
* **Dynamic Asset Weighting:** Automatically adjusts equal weighting ($1/N$) across any combination of tickers entered in the sidebar.
* **Interactive Visualizations:** Plots daily return histograms with dashed VaR cutoffs and dynamic asset correlation matrices using Plotly.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Frontend/UI:** Streamlit
* **Financial Data:** yFinance
* **Data Manipulation & Analytics:** Pandas, NumPy, SciPy
* **Visualization:** Plotly Express

---

git clone [https://github.com/Niham123/var-risk-analytics-dashboard.git](https://github.com/Niham123/var-risk-analytics-dashboard.git)
cd var-risk-analytics-dashboard
