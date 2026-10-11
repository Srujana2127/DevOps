# Exercise 1: Hello Pod — Kubernetes Getting Started

## Objective

Deploy an Nginx web server inside a Kubernetes Pod, expose it using a NodePort Service, and access the application through Minikube.

## Environment

* Operating System: Windows 11 with Ubuntu 22.04 on WSL
* Kubernetes Cluster: Minikube
* Container Runtime: Docker
* Application: Nginx
* Service Type: NodePort

## Implementation Steps

### 1. Start Minikube

Started a local Kubernetes cluster using the Docker driver.

```bash
minikube start --driver=docker
```

### 2. Create the Pod

Created a Pod named `hello-k8s` using the Nginx image.

```bash
minikube kubectl -- run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod

Checked the Pod status to confirm that the application was running.

```bash
minikube kubectl -- get pods
```

**Result:** The `hello-k8s` Pod reached `Running` status and showed `1/1` containers ready.

### 4. Expose the Pod

Created a NodePort Service to expose the Nginx application on port 80.

```bash
minikube kubectl -- expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Service

Listed the Kubernetes Services.

```bash
minikube kubectl -- get services
```

**Result:** The `hello-k8s` Service was created with type `NodePort`, exposing port `80` through NodePort `32606`.

### 6. Access the Application

Used Minikube to open the exposed service.

```bash
minikube service hello-k8s
```

The service can be accessed using the local URL provided by Minikube while its tunnel is running. The expected page is the Nginx welcome page.

## Outcome

Successfully created and verified a Kubernetes Pod running Nginx, exposed it through a NodePort Service, and configured local access using Minikube.

## Concepts Learned

* Kubernetes Pods and containers
* Deploying an application using a container image
* Kubernetes Services
* NodePort networking
* Running a local Kubernetes cluster with Minikube
* Verifying Pods and Services using kubectl through Minikube

