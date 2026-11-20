
from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 201
    assert response.json["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 201
    assert response.json["status"] == "healthy"


def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"delivery_requests_total" in response.data
    assert b"delivery_queue_size" in response.data
