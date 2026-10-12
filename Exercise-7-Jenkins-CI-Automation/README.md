# Exercise 7: Jenkins CI Automation

## Overview
This project demonstrates Continuous Integration (CI) using Jenkins,
a Python application, unit tests, and Docker.

## Project Structure
- `app.py` - Python application containing an addition function.
- `test_app.py` - Unit tests for the application.
- `Jenkinsfile` - Declarative Jenkins pipeline.
- `Dockerfile` - Jenkins image configuration.
- `compose.yaml` - Docker Compose configuration for Python tests.
- `README.md` - Project documentation.

## Requirements
- Docker Desktop or Docker Engine
- Jenkins
- Internet connection to download the Python Docker image

## Run the Application
From the project directory, run:

    docker run --rm -v "$PWD:/app" -w /app python:3.12-slim python app.py

Expected output:

    Jenkins CI Automation
    2 + 3 = 5

## Run Unit Tests
Run:

    docker run --rm -v "$PWD:/app" -w /app python:3.12-slim python -m unittest -v

The test suite contains two tests:
- `test_add` verifies that 2 + 3 equals 5.
- `test_add_zero` verifies that adding zero preserves the number.

Both tests have been verified successfully in the Python 3.12 Docker image.

## Docker Compose
To run the tests using Docker Compose:

    docker compose run --rm python-tests

## Jenkins Pipeline
The Jenkins job demonstrates a Declarative Pipeline with stages for
pipeline initialization, project configuration verification, and completion.

The current Jenkins job is a demonstration pipeline. The Python unit tests
were verified separately in Docker and are not currently executed by the
Jenkins job itself.

## Learning Outcomes
- Understanding Continuous Integration
- Creating a Declarative Jenkins Pipeline
- Writing Python unit tests with `unittest`
- Running Python applications and tests in Docker
- Documenting a CI project
