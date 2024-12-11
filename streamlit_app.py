import streamlit as st
from services import fetch_stock_data, process_stock_data, calculate_moving_average, calculate_rsi, add_technical_indicators

st.title("Stock Explorer and Analysis App")
st.write("""
Explore stock data and generate interactive charts.
""")

st.sidebar.header("Stock Selector")
ticker_input = st.sidebar.text_input("Enter Stock Tickers (comma-separated):", value="AAPL, MSFT, GOOG")
timeframe = st.sidebar.selectbox("Select Timeframe:", ["1 Month", "3 Months", "6 Months", "1 Year", "All Time"], index=2)
show_range = st.sidebar.checkbox("Show Day's High and Low Range")
tickers = [ticker.strip().upper() for ticker in ticker_input.split(",") if ticker.strip()]

if st.sidebar.button("Analyze Stocks"):
    if not tickers:
        st.error("Please enter at least one stock ticker.")
    else:
        try:
            stock_data = fetch_stock_data(tickers, timeframe)
        except Exception as e:
            st.error(f"Failed to fetch stock data: {e}")
            st.stop()

        combined_data = process_stock_data(stock_data)

        for ticker, data in stock_data.items():
            with st.expander(f"View Details for {ticker}", expanded=False):
                st.write(f"### {timeframe} Chart of {ticker}")
                st.line_chart(data["Close"], height=300, use_container_width=True)

                rsi = calculate_rsi(data["Close"])
                moving_average = calculate_moving_average(data["Close"])
                st.write(f"#### RSI and Moving Average for {ticker}")
                st.line_chart(rsi, height=150, use_container_width=True)
                st.line_chart(moving_average, height=150, use_container_width=True)

                if show_range:
                    st.write(f"#### Day's High, Low, and Range for {ticker}")
                    data["Range"] = data["High"] - data["Low"]
                    data["RangePercentage"] = (data["High"] - data["Low"])/data["Low"] * 100
                    range_df = data[["High", "Low", "Range", "RangePercentage"]]
                    st.dataframe(range_df.tail(10))


        if not combined_data.empty:
            st.write("### Combined Price Chart")
            st.line_chart(combined_data, height=400, use_container_width=True)
