# Secure Multi-Stage Dockerized Application

This repository demonstrates advanced containerization techniques by packaging a Python web application using Docker multi-stage builds and a Google Distroless runtime environment. 

The primary focus of this project is to showcase security-first infrastructure practices, image size optimization, and modern container orchestration.

##  Architecture & DevOps Practices

This project implements several industry-standard containerization best practices:

* **Multi-Stage Builds:** The `Dockerfile` is split into two stages. Stage I handles the compilation and installation of dependencies, while Stage II only copies the necessary compiled artifacts to the final image. This keeps build tools out of the production environment.
* **Distroless Runtime (`gcr.io/distroless/python3-debian12`):** The final production image uses a Distroless base. By stripping out package managers (like `apt`), shells (like `bash`), and standard Linux utilities, the container's attack surface is drastically reduced.
* **Least Privilege Principle:** The container is designed to run only the application itself, minimizing potential security vulnerabilities.
* **Container Orchestration:** A `docker-compose.yml` file is provided for seamless, reproducible deployments and port mapping.

##  Infrastructure Stack

* **Containerization:** Docker
* **Base Images:** * Build Stage: `python:3.13-slim`
  * Runtime Stage: `gcr.io/distroless/python3-debian12`
* **Orchestration:** Docker Compose
* **Application Framework:** Python / Flask (Proof of Concept)

##  Deployment Instructions

### Option 1: Deploying via Docker Compose (Recommended)

The most efficient way to spin up the application is using Docker Compose. This will automatically pull the specified image (`syedshakir1/python-flask-app:latest`) and map the required ports.

1. Ensure the `docker-compose.yml` file is in your working directory.
2. Start the service in detached mode:
   ```bash
   docker-compose up -d
3. To stop & remove the container:
   ```bash
   docker-compose down
