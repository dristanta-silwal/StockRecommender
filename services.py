import yfinance as yf
import pandas as pd

PERIOD_MAP = {
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "All Time": "max"
}

def fetch_stock_data(tickers, timeframe):
    """Fetch stock data for a list of tickers and timeframe."""
    stock_data = {}
    period = PERIOD_MAP.get(timeframe, "1y")
    for ticker in tickers:
        try:
            data = yf.download(ticker, period=period, progress=False)
            if not data.empty:
                stock_data[ticker] = data
            else:
                print(f"No data found for {ticker}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return stock_data

def process_stock_data(stock_data):
    """Process stock data to prepare it for visualization or clustering."""
    combined_data = pd.DataFrame()
    for ticker, data in stock_data.items():
        combined_data[ticker] = data["Close"]
    return combined_data

def calculate_moving_average(data, window=14, ma_type="SMA"):
    if ma_type == "SMA":
        return data.rolling(window=window).mean()
    elif ma_type == "EMA":
        return data.ewm(span=window, adjust=False).mean()
    else:
        raise ValueError("ma_type must be 'SMA' or 'EMA'")

def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

def add_technical_indicators(data, ma_windows=None, rsi_window=14):
    ma_windows = ma_windows or [14, 50, 200]

    for window in ma_windows:
        data[f"SMA_{window}"] = calculate_moving_average(data["Close"], window=window, ma_type="SMA")
        data[f"EMA_{window}"] = calculate_moving_average(data["Close"], window=window, ma_type="EMA")

    data["RSI"] = calculate_rsi(data["Close"], window=rsi_window)

    return data
