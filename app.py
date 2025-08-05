# app.py

import streamlit as st
from strategy_engine import calculate_payoff, plot_payoff
from data_loader import load_sample_data

st.set_page_config(page_title="Hedging Strategy Simulator", layout="wide")

st.title("📈 Hedging Strategy & Options Payoff Simulator")

# Sidebar for selections
strategy = st.sidebar.selectbox("Choose Strategy", ["Protective Put", "Covered Call", "Collar"])
contract_month = st.sidebar.selectbox("Select Contract Duration", ["1-Month", "2-Month"])

stock = st.sidebar.selectbox("Choose Stock", ["RELIANCE", "INFY", "HDFCBANK"])
strike_price = st.sidebar.slider("Select Strike Price", 1000, 4000, 2500, step=50)
premium = st.sidebar.number_input("Enter Premium", value=100)
lot_size = st.sidebar.number_input("Lot Size", value=50)

# Load dummy stock data (can be replaced with NSE API later)
price_range = load_sample_data(stock)

# Calculate Payoff
payoff_df = calculate_payoff(strategy, price_range, strike_price, premium, lot_size)

# Plot Payoff
plot_payoff(payoff_df, strategy)

st.markdown("### 📌 Explanation:")
st.write(f"Strategy: **{strategy}**, Stock: **{stock}**, Duration: **{contract_month}**")
