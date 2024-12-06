import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Stock Explorer and Analysis App")
st.write("""
A tool for exploring stock data, generating interactive charts, 
and performing technical analysis for selected tickers.
""")

st.sidebar.header("Stock Selector")
ticker_input = st.sidebar.text_input("Enter Stock Tickers (comma-separated):", value="AAPL, MSFT, GOOG")
timeframe = st.sidebar.selectbox("Select Timeframe:", ["1 Month", "3 Months", "6 Months", "1 Year", "All Time"])
tickers = [ticker.strip().upper() for ticker in ticker_input.split(",") if ticker.strip()]

if st.sidebar.button("Analyze Stocks"):
    if not tickers:
        st.error("Please enter at least one stock ticker.")
    else:
        st.write(f"### Selected Stocks: {', '.join(tickers)}")
        st.write(f"### Timeframe: {timeframe}")

        def fetch_stock_data(ticker, timeframe):
            period_map = {
                "1 Month": "1mo",
                "3 Months": "3mo",
                "6 Months": "6mo",
                "1 Year": "1y",
                "All Time": "max"
            }
            return yf.download(ticker, period=period_map[timeframe])

        combined_data = pd.DataFrame()

        try:
            for ticker in tickers:
                data = fetch_stock_data(ticker, timeframe)
                if data.empty:
                    st.warning(f"No data found for {ticker}. Skipping...")
                    continue
                
                combined_data[ticker] = data["Close"]
                st.write(f"#### {ticker}")
                st.dataframe(data.tail(10))
                st.write(f"Price Chart for {ticker}")
                plt.figure(figsize=(10, 5))
                plt.plot(data.index, data["Close"], label="Close Price")
                plt.title(f"{ticker} Price Chart")
                plt.xlabel("Date")
                plt.ylabel("Price")
                plt.legend()
                st.pyplot(plt)

            if not combined_data.empty:
                st.write("### Combined Price Chart")
                plt.figure(figsize=(12, 6))
                for ticker in combined_data.columns:
                    plt.plot(combined_data.index, combined_data[ticker], label=ticker)
                plt.title("Combined Stock Prices")
                plt.xlabel("Date")
                plt.ylabel("Price")
                plt.legend()
                st.pyplot(plt)

        except Exception as e:
            st.error(f"An error occurred: {e}")
