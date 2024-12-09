import streamlit as st
from services import fetch_stock_data, process_stock_data

st.title("Stock Explorer and Analysis App")
st.write("""
Explore stock data and generate interactive charts.
""")

st.sidebar.header("Stock Selector")
ticker_input = st.sidebar.text_input("Enter Stock Tickers (comma-separated):", value="AAPL, MSFT, GOOG")
timeframe = st.sidebar.selectbox("Select Timeframe:", ["1 Month", "3 Months", "6 Months", "1 Year", "All Time"])
tickers = [ticker.strip().upper() for ticker in ticker_input.split(",") if ticker.strip()]

if st.sidebar.button("Analyze Stocks"):
    if not tickers:
        st.error("Please enter at least one stock ticker.")
    else:
        stock_data = fetch_stock_data(tickers, timeframe)
        combined_data = process_stock_data(stock_data)

        for ticker, data in stock_data.items():
            st.write(f"### {ticker}")
            st.line_chart(data["Close"], height=300, use_container_width=True)

        if not combined_data.empty:
            st.write("### Combined Price Chart")
            st.line_chart(combined_data, height=400, use_container_width=True)
