from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Prometheus metric
REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

@app.route("/")
def home():
    REQUESTS.labels(method="GET", endpoint="/").inc()
    return jsonify({
        "service": "Agricultural Product Platform",
        "status": "running",
        "message": "Daily product list is available"
    })

@app.route("/products")
def products():
    REQUESTS.labels(method="GET", endpoint="/products").inc()
    return jsonify([
        {"name": "Wheat", "price": 250},
        {"name": "Corn", "price": 180},
        {"name": "Rice", "price": 300}
    ])

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
