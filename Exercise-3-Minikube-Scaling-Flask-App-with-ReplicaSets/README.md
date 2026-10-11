# Exercise 3: Minikube Scaling Flask App with ReplicaSets

## Objective

Deploy a Flask flash-sale application on Kubernetes using Minikube and a ReplicaSet. Scale the application from three to five replicas and verify automatic Pod replacement.

## Technologies

* Python
* Flask
* Docker
* Kubernetes
* Minikube

## Project Files

* `app.py` — Flask application with home, buy, and health endpoints.
* `Dockerfile` — Builds the Flask application image.
* `replicaset.yaml` — Configures the ReplicaSet with three initial replicas.
* `service.yaml` — Exposes the application through a NodePort Service.

## Implementation Steps

1. Built the Docker image `flashsale:v1`.
2. Created the Kubernetes ReplicaSet with three replicas.
3. Verified that all three Flask Pods were running.
4. Exposed the application using a NodePort Service.
5. Tested the Flask application through the Minikube Service URL.
6. Scaled the ReplicaSet from three to five replicas.
7. Deleted one Pod and verified that Kubernetes created a replacement.

## Useful Commands

Build the image:

```bash
minikube image build -t flashsale:v1 .
```

Deploy the ReplicaSet:

```bash
minikube kubectl -- apply -f replicaset.yaml
```

Deploy the Service:

```bash
minikube kubectl -- apply -f service.yaml
```

Scale to five replicas:

```bash
minikube kubectl -- scale replicaset flashsale-replicaset --replicas=5
```

Check replicas:

```bash
minikube kubectl -- get replicasets
```

Check application Pods:

```bash
minikube kubectl -- get pods -l app=flashsale
```

## Result

The Flask application was deployed successfully on Minikube. The ReplicaSet maintained five running replicas after scaling, and Kubernetes automatically created a replacement Pod after one Pod was deleted.
