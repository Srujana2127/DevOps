from flask import Flask, jsonify
import socket

app = Flask(__name__)

# Sample inventory data
inventory = [
    {
        "product_id": 101,
        "product_name": "Laptop",
        "quantity": 25,
        "price": 55000
    },
    {
        "product_id": 102,
        "product_name": "Mobile Phone",
        "quantity": 40,
        "price": 20000
    },
    {
        "product_id": 103,
        "product_name": "Headphones",
        "quantity": 60,
        "price": 2500
    }
]

@app.route("/")
def home():
    return "E-Commerce Inventory Service is Running!"

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify({
        "status": "success",
        "pod_name": socket.gethostname(),
        "inventory": inventory
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
