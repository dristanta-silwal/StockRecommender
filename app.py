from flask import Flask, request, jsonify
import yfinance as yf
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

def fetch_stock_data(tickers):
    stock_data = {}
    for ticker in tickers:
        data = yf.download(ticker, period="1y")
        stock_data[ticker] = data
    return stock_data

def cluster_stocks(data):
    metrics = []
    for ticker, stock in data.items():
        mean_return = stock["Adj Close"].pct_change().mean() if not stock["Adj Close"].empty else 0
        volatility = stock["Adj Close"].pct_change().std() if not stock["Adj Close"].empty else 0

        metrics.append({
            "Ticker": ticker,
            "Mean_Return": float(mean_return),
            "Volatility": float(volatility)
        })
    df = pd.DataFrame(metrics)

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[["Mean_Return", "Volatility"]])

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(scaled_data)

    return df

@app.route("/cluster", methods=["POST"])
def cluster_endpoint():
    request_data = request.json
    tickers = request_data.get("tickers", [])
    if not tickers:
        return jsonify({"error": "No tickers provided"}), 400

    try:
        stock_data = fetch_stock_data(tickers)
        clustered_data = cluster_stocks(stock_data)

        result = clustered_data.to_dict(orient="records")
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
