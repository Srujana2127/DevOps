# Jenkins Pipeline for a Metrics Exporter

## 1. Project Overview

This project automates the build, testing, validation and deployment packaging of a Python-based Delivery Metrics Exporter using Jenkins Pipeline.

The application exposes delivery-related metrics in Prometheus-compatible format through a REST endpoint.

## 2. Objective

- Develop a Python Metrics Exporter.
- Store the project and Jenkinsfile in GitHub.
- Automate source checkout and dependency installation.
- Perform application build and automated testing.
- Generate a runnable deployment artifact.
- Demonstrate Jenkins failure handling using a controlled test failure.

## 3. Technologies Used

- Python
- Flask
- Prometheus Client
- Pytest
- Jenkins
- GitHub
- Linux / Ubuntu

## 4. Project Structure

```text
Question-4-Metrics-Exporter/
├── app.py
├── requirements.txt
├── test_app.py
├── Jenkinsfile
├── README.md
└── deployment/
```

## 5. Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Displays application information |
| `/health` | Checks application health |
| `/metrics` | Exposes Prometheus metrics |

## 6. Jenkins Pipeline Stages

1. Checkout – Retrieves source code from GitHub.
2. Install Dependencies – Installs Python packages.
3. Build – Validates Python syntax and prepares deployment directory.
4. Test – Runs automated tests using Pytest.
5. Package Deployment – Copies application files and creates a compressed deployment artifact.

## 7. Local Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

Run application:

```bash
python app.py
```

Open:

- http://localhost:8001/
- http://localhost:8001/health
- http://localhost:8001/metrics

## 8. Expected Result

- Jenkins successfully retrieves the GitHub repository.
- Python dependencies are installed.
- Application build and validation succeed.
- Automated tests pass.
- Deployment artifact `metrics-exporter.tar.gz` is generated.
- A controlled test failure causes Jenkins to report FAILED.
- After correcting the failure, the pipeline reports SUCCESS.

## 9. Conclusion

This project demonstrates Jenkins-based Continuous Integration and deployment packaging for a Python Metrics Exporter. It automates source checkout, dependency installation, build validation, testing and artifact generation while demonstrating failure detection and recovery.
