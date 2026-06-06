import streamlit as st
import pandas as pd

st.title("Bluestock Mutual Fund Analytics Dashboard")

cagr = pd.read_csv(r"C:\Users\swamy\Downloads\bluestack_mf_capstone\reports\top_cagr_funds.csv")
sharpe = pd.read_csv(r"C:\Users\swamy\Downloads\bluestack_mf_capstone\reports\sharpe_ratio_ranking.csv")
drawdown = pd.read_csv(r"C:\Users\swamy\Downloads\bluestack_mf_capstone\reports\max_drawdown.csv")
daily = pd.read_csv(r"C:\Users\swamy\Downloads\bluestack_mf_capstone\reports\top_funds_daily_return.csv")
st.header("Top CAGR Funds")
st.dataframe(cagr.head(10))

st.header("Top Sharpe Ratio Funds")
st.dataframe(sharpe.head(10))

st.header("Maximum Drawdown")
st.dataframe(drawdown.head(10))

st.title("📊 Bluestock Mutual Fund Analytics Dashboard")

st.subheader("🏆 Top CAGR Funds")
st.dataframe(cagr)

st.subheader("⭐ Top Sharpe Ratio Funds")
st.dataframe(sharpe)

st.subheader("📉 Maximum Drawdown")
st.dataframe(drawdown)

st.subheader("🚀 Top Daily Return Funds")
st.dataframe(daily)