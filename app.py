from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Agricultural Product Platform",
        "status": "running",
        "message": "Daily product list is available"
    })

@app.route("/products")
def products():
    return jsonify([
        {"name": "Wheat", "price": 250},
        {"name": "Corn", "price": 180},
        {"name": "Rice", "price": 300}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

