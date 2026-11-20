
from flask import Flask, Response, jsonify
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "delivery_requests_total",
    "Total number of delivery requests"
)

QUEUE_SIZE = Gauge(
    "delivery_queue_size",
    "Current number of pending deliveries"
)

QUEUE_SIZE.set(5)


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "application": "Delivery Metrics Exporter",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
