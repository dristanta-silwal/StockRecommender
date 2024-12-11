# [Stock Explorer and Analysis App](https://stockrecommender.streamlit.app/)
View Live: [Stock Recommender](https://stockrecommender.streamlit.app/)

## Overview
The Stock Explorer and Analysis App is a tool built with Python and Streamlit that allows users to explore stock data, generate interactive charts, and perform technical analysis for selected stock tickers. The app integrates with Yahoo Finance to fetch real-time stock data and display key metrics for user-selected timeframes.

This project is designed for investors, traders, and enthusiasts who want to analyze stock performance efficiently and visually.

---

## Features
- Search Stocks: Enter stock tickers (e.g., `AAPL, MSFT, TSLA`) to analyze their performance.
- Custom Timeframes: Analyze data for the following periods:
  - 1 Month
  - 3 Months
  - 6 Months
  - 1 Year
  - All Time
- Individual Stock Analysis:
  - Raw data table for each stock.
  - Interactive price charts.
  - Moving averages (e.g., 20-day, 50-day) for technical analysis.
- Combined Stock Chart:
  - Compare the performance of multiple stocks on a single graph.
- Real-Time Data: Fetches the latest stock information from Yahoo Finance using the `yfinance` library.
- Error Handling: Skips invalid tickers and notifies users if data is unavailable.

---

## Technology Stack
- Frontend: [Streamlit](https://streamlit.io/) for building an interactive web-based UI.
- Backend: Python logic to fetch and process stock data.
- Data Source: [Yahoo Finance](https://finance.yahoo.com/) via the `yfinance` library.
- Visualization: Matplotlib for generating interactive plots.

---

## Installation
### Prerequisites
- Python 3.7 or higher installed on your system.
- Basic knowledge of running Python scripts and packages.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/dristanta-silwal/stock-explorer-app.git
   cd stock-explorer-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app locally:
   ```bash
   streamlit run streamlit_app.py
   ```

5. Open the app in your browser using the URL displayed in the terminal (default: `http://localhost:8501`).

---

## How to Use
1. Enter Stock Tickers: Use the sidebar to enter stock tickers (comma-separated). Example: `AAPL, MSFT, TSLA`.
2. Select Timeframe: Choose the desired timeframe from the dropdown menu.
3. Analyze Stocks:
   - Click the "Analyze Stocks" button to fetch and display data.
   - View raw data, individual stock charts, and a combined price chart for selected tickers.
4. Explore Technical Analysis:
   - Check moving averages (20-day and 50-day) for individual stocks.
   - Visualize trends and compare multiple stocks in the combined chart.

---

## Project Structure
```
stock-explorer-app/
├── streamlit_app.py       # Main application script
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## Dependencies
The following Python packages are required to run this app:
- `streamlit`: For creating the web-based interface.
- `pandas`: For data manipulation and analysis.
- `yfinance`: For fetching real-time stock data from Yahoo Finance.
- `matplotlib`: For generating stock price and technical analysis charts.

---

## Key Functions
### `fetch_stock_data(ticker, timeframe)`
- Fetches stock data for a given ticker and timeframe using the `yfinance` library.
- Maps timeframes to Yahoo Finance-compatible periods (`1mo`, `3mo`, etc.).

### `combined_price_chart`
- Plots the closing prices of all selected tickers on a single graph.
- Uses Pandas for alignment and Matplotlib for visualization.

### `moving_averages`
- Calculates and plots 20-day and 50-day simple moving averages for individual stocks.
- Helps users identify trends and support/resistance levels.

---

## Future Enhancements
1. Advanced Technical Indicators:
   - Add Bollinger Bands, RSI, MACD, etc.
2. Portfolio Analysis:
   - Allow users to input a portfolio of stocks and analyze performance.
3. Historical Data Downloads:
   - Provide an option to download raw data as a CSV file.
4. Integration with APIs:
   - Fetch additional data like news, financial statements, or sector performance.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Acknowledgments
- [Streamlit](https://streamlit.io/): For providing an easy-to-use Python library for building web apps.
- [Yahoo Finance](https://finance.yahoo.com/): For access to financial data via the `yfinance` library.
- Open-source community for inspiration and guidance.
