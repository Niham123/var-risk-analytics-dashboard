
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import norm
import plotly.express as px

st.set_page_config(page_title="Quantitative Risk Dashboard", layout="wide")
st.title("📊 Quantitative Risk & VaR Analytics Dashboard")

# Sidebar inputs
st.sidebar.header("Portfolio Settings")
tickers_input = st.sidebar.text_input("Enter Tickers (comma-separated)", "AAPL, MSFT, GOOGL, AMZN")
tickers = [t.strip().upper() for t in tickers_input.split(",")]
confidence_level = st.sidebar.slider("Confidence Level", 0.90, 0.99, 0.95, 0.01)
portfolio_value = st.sidebar.number_input("Portfolio Value ($)", value=1000000, step=50000)

# Fetch historical data
@st.cache_data
def load_data(symbols):
    data = yf.download(symbols, period="2y")['Close']
    return data

data = load_data(tickers)
returns = data.pct_change().dropna()

# Equal weighting
weights = np.array([1 / len(tickers)] * len(tickers))
portfolio_returns = returns.dot(weights)

# Calculations
mean_return = portfolio_returns.mean()
std_dev = portfolio_returns.std()

# 1. Parametric VaR & CVaR
z_score = norm.ppf(1 - confidence_level)
var_parametric = -(mean_return + z_score * std_dev) * portfolio_value
cvar_parametric = portfolio_value * (std_dev * (norm.pdf(z_score) / (1 - confidence_level)) - mean_return)

# 2. Historical VaR & CVaR
var_historical = -np.percentile(portfolio_returns, (1 - confidence_level) * 100) * portfolio_value
cvar_historical = -portfolio_returns[portfolio_returns <= -var_historical / portfolio_value].mean() * portfolio_value

# Layout Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Parametric VaR", f"${var_parametric:,.2f}")
col2.metric("Parametric CVaR", f"${cvar_parametric:,.2f}")
col3.metric("Historical VaR", f"${var_historical:,.2f}")
col4.metric("Historical CVaR", f"${cvar_historical:,.2f}")

# Distribution Chart
st.subheader("Portfolio Daily Return Distribution vs. VaR Cutoff")
fig = px.histogram(portfolio_returns, nbins=50, title="Daily Returns Histogram", labels={'value': 'Daily Return'})
fig.add_vline(x=-var_historical / portfolio_value, line_dash="dash", line_color="red", annotation_text="Historical VaR Cutoff")
st.plotly_chart(fig, use_container_width=True)

# Correlation Matrix
st.subheader("Asset Correlation Matrix")
st.plotly_chart(px.imshow(returns.corr(), text_auto=True, color_continuous_scale="Blues"), use_container_width=True)