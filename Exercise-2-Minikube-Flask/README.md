# Exercise 2: Deploy Flask Application on Minikube

## Aim

To build a Docker image for a Flask application and deploy it on Kubernetes using Minikube.

## Technologies Used

* Python and Flask
* Docker
* Kubernetes
* Minikube
* kubectl

## Project Files

* `app.py` – Flask application.
* `Dockerfile` – Instructions to build the Docker image.
* `flask-deployment.yaml` – Kubernetes Deployment and Service configuration.

## Application Output

The Flask application displays the following message when accessed successfully:

**Hello from Flask on Kubernetes!**

## Steps Performed

### 1. Start Minikube

```bash
minikube start
```

### 2. Build the Docker Image

```bash
docker build -t flask-app:latest .
```

### 3. Deploy the Application

```bash
minikube kubectl -- apply -f flask-deployment.yaml
```

### 4. Check the Deployment

```bash
minikube kubectl -- get deployments
```

### 5. Check the Pods

```bash
minikube kubectl -- get pods
```

### 6. Check the Services

```bash
minikube kubectl -- get services
```

### 7. Access the Application

```bash
minikube service flask-app-service --url
```

Open the URL displayed in the terminal in a browser to view the Flask application.

## Result

The Flask application was successfully built into a Docker image, deployed on Minikube, and accessed through a Kubernetes Service.

