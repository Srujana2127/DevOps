
# Exercise 6: Grafana Real-Time Monitoring of a Quick-Commerce App

## Objective
Build a containerized quick-commerce monitoring demo using Python,
Prometheus, Grafana, and Jenkins pipeline validation.

## Architecture
Python Flask App -> Prometheus -> Grafana Dashboard

The Python application simulates order and delivery activity.
Prometheus scrapes application metrics every 5 seconds.
Grafana visualizes delivery counts, order counts, and delivery duration.

## Technologies
- Python 3.10
- Flask
- Prometheus
- Grafana
- Docker and Docker Compose
- Jenkins

## Project Structure
- delivery_metrics.py: Simulated delivery application and metrics endpoint
- requirements.txt: Python dependencies
- Dockerfile: Application container definition
- compose.yaml: Application, Prometheus, and Grafana services
- prometheus.yml: Prometheus scrape configuration
- alert_rules.yml: Monitoring alert rules
- grafana/provisioning/datasources/prometheus.yml: Data source
- grafana/provisioning/dashboards/dashboard.yml: Dashboard provisioning
- grafana/dashboards/quick-commerce.json: Dashboard panels
- Jenkinsfile: Validation pipeline

## Run the Project
Start all services:

    docker compose up -d --build

Check container status:

    docker compose ps

Application:
- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/metrics

Prometheus:
- http://localhost:9090
- http://localhost:9090/targets

Grafana:
- http://localhost:3000

Local demo credentials:
- Username: admin
- Password: admin123

Change these credentials before any shared or public deployment.

## Stop the Project

    docker compose down

## Notes
The application generates simulated data for learning and demonstration.
Jenkins validation requires a configured Jenkins agent with Docker access.
