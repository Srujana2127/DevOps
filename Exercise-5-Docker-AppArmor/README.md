# Docker Security with AppArmor and Python

## Objective
Secure a Flask application in Docker using an AppArmor profile and the Docker SDK for Python.

## Project Files
- app.py: Flask web application.
- Dockerfile: Builds the Docker image.
- my-apparmor-profile: AppArmor security policy.
- apply_apparmor.py: Starts the container and inspects its security options.
- test_restricted_actions.py: Tests restricted file access and shell execution.

## Requirements
- Docker
- Python 3
- Docker SDK for Python
- AppArmor-enabled Linux host

## Build the Docker Image
    docker build -t flask-apparmor .

## Install Docker SDK
    python3 -m pip install docker

## Load the AppArmor Profile
On a supported Linux host, validate and load the profile:
    sudo apparmor_parser -r ./my-apparmor-profile

## Run the Python Scripts
    python3 apply_apparmor.py
    python3 test_restricted_actions.py

## Environment and Test Status
Development environment: Ubuntu on WSL2, Docker 29.1.3,
Docker SDK for Python 7.2.0.

The AppArmor kernel parameter reported N, and aa-status reported
that the AppArmor filesystem was not mounted. Therefore, enforcement
and restricted-action tests have not been verified in this environment.

A successful Docker container start does not prove AppArmor enforcement.
Repeat the security tests on a Linux host with AppArmor enabled before
marking them as passed.
