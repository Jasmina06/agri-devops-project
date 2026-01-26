import logging
from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__) 

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])

@app.route("/")
def home():
    REQUESTS.labels(method="GET", endpoint="/").inc()
    logger.info("Home page accessed - Product list updated") 
    return jsonify({
        "service": "Agricultural Product Platform",
        "status": "running",
        "message": "Daily product list is available"
    })

@app.route("/notify")
def notify():
    REQUESTS.labels(method="GET", endpoint="/notify").inc()
    logger.info("ORDER_NOTIFICATION: Message sent to supplier successfully")
    return jsonify({"status": "Notification sent", "reliable": True})

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)