# Exercise 7: Jenkins CI Automation

## Objective

Understand Continuous Integration (CI) and install Jenkins using Docker.

## Concepts Covered

* Continuous Integration (CI)
* Automated builds and testing
* Jenkins jobs, builds, pipelines, and plugins
* Jenkins installation using Docker

## Prerequisites

* Ubuntu / WSL
* Docker

## Jenkins Installation

Run Jenkins in a Docker container:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

Check the running container:

```bash
docker ps
```

Retrieve the initial administrator password:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open Jenkins in a browser:

http://localhost:8080

## Setup Completed

* Jenkins container started successfully.
* Jenkins initial setup completed.
* Suggested plugins installed.
* Jenkins dashboard accessed successfully.

## Result

Jenkins was installed and configured successfully using Docker. The Jenkins dashboard is accessible locally on port 8080.

## Security Note

Do not store administrator passwords or other secrets in this repository.
