from flask import Flask, request, jsonify
from services import fetch_stock_data, process_stock_data

app = Flask(__name__)

@app.route("/stocks", methods=["POST"])
def fetch_stocks():
    request_data = request.json
    tickers = request_data.get("tickers", [])
    timeframe = request_data.get("timeframe", "1 Year")

    if not tickers:
        return jsonify({"error": "No tickers provided"}), 400

    try:
        stock_data = fetch_stock_data(tickers, timeframe)
        processed_data = process_stock_data(stock_data)
        return jsonify(processed_data.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
