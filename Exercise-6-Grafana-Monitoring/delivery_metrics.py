
from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import threading
import time

app = Flask(__name__)

deliveries_total = Counter(
    "quickcommerce_deliveries_total",
    "Total number of completed deliveries"
)

delivery_time = Histogram(
    "quickcommerce_delivery_duration_seconds",
    "Delivery duration in seconds",
    buckets=(300, 600, 900, 1200, 1800, 2400, 3600)
)

orders_total = Counter(
    "quickcommerce_orders_total",
    "Total number of orders received"
)

def simulate_deliveries():
    while True:
        orders_total.inc()
        duration = random.uniform(300, 2400)
        delivery_time.observe(duration)
        deliveries_total.inc()
        time.sleep(5)

@app.route("/")
def home():
    return jsonify({
        "application": "Quick-Commerce Monitoring",
        "status": "running",
        "metrics_endpoint": "/metrics"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    threading.Thread(target=simulate_deliveries, daemon=True).start()
    app.run(host="0.0.0.0", port=8000)
