# Exercise 9: Jenkins Multi-Stage Pipeline

## Objective
Create a Jenkins multi-stage pipeline for a Flask web application.

## Technologies
- Jenkins
- Docker
- Docker Compose
- Python
- Flask
- Unit Testing

## Project Files
- app.py: Flask web application
- test_app.py: Unit tests
- requirements.txt: Python dependencies
- Dockerfile: Docker image instructions
- compose.yaml: Docker Compose configuration
- Jenkinsfile: Jenkins pipeline definition
- README.md: Project documentation

## Jenkins Stages
1. Build
2. Test
3. Deploy
4. Run Application
5. Verify

## Run the Application
Build the image using: docker build -t exercise9-flask-app .

Run the tests using: docker run --rm exercise9-flask-app python -m unittest test_app.py

Start the application using: docker compose up -d

Open http://localhost:5001 in your browser.
