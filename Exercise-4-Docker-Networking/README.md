# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker bridge networking and configure a multi-container application.

## Architecture
- Flask: REST API running on port 5001
- MySQL: Database service running on port 3306
- Redis: Cache service running on port 6379
- Network: my-bridge-net (bridge driver)

## Files
- app.py: Flask REST API
- requirements.txt: Python dependencies
- Dockerfile: Builds the Flask image

## Steps Performed

### 1. Create and inspect the network
```bash
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

### 2. Build the Flask image
```bash
docker build -t flask-api .
```

### 3. Start the containers
```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabPass123! mysql:latest
docker run -d --name redis --network my-bridge-net redis:latest
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### 4. Test the Flask API
Open http://localhost:5001/about in a browser.

Expected response:
```json
{
  "name": "Simple REST API",
  "version": "1.0",
  "description": "This is a simple REST API built with Flask."
}
```

### 5. Test container connectivity
```bash
docker exec flask python -c "import socket; print('MySQL:', socket.gethostbyname('mysql')); print('Redis:', socket.gethostbyname('redis'))"
```

Test service ports:
```bash
docker exec flask python -c "import socket; s=socket.create_connection(('mysql',3306),timeout=5); print('MySQL connection successful'); s.close(); s=socket.create_connection(('redis',6379),timeout=5); print('Redis connection successful'); s.close()"
```

Both service connections were successful.

## Questions and Answers

### 1. What is the purpose of the --net flag in docker run?
It connects a container to a specified Docker network. The equivalent option used in this lab is --network.

### 2. How do containers communicate on the same network?
Containers on a user-defined bridge network can communicate using their container names or IP addresses. Docker provides internal DNS resolution for container names.

### 3. What is the difference between bridge and host networking?
A bridge network connects containers through an isolated virtual network managed by Docker. Host networking shares the host's network stack and does not provide the same network isolation.

### 4. How can you expose a container's port to the host?
Use the -p option, such as -p 5001:5001, to map host port 5001 to container port 5001.

## Cleanup
After capturing the results, the containers and network can be removed with:

```bash
docker stop mysql redis flask
docker rm mysql redis flask
docker network rm my-bridge-net
```
