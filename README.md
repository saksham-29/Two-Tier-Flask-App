**Two Tier Flask Application with Automated CI/CD using GitHub Actionson on AWS**

**Author:** Saksham Saxena
**Date:** December 24, 2025

This project demonstrates a production-style two-tier web application built using Flask and MySQL, containerized with Docker, orchestrated using Docker Compose, and deployed automatically to AWS EC2 through a GitHub Actions CI/CD pipeline.

The primary objective of this project is to showcase real-world DevOps practices, including containerization, automation, and cloud deployment.

**Architecture Overview**

Developer Push (main)
→ GitHub Actions (CI/CD)
→ AWS EC2 (Ubuntu)
→ Docker Compose
→ Flask Application (Port 5000) + MySQL Database (Persistent Volume)

**Tools & Technologies Used**

Application
│
├── Backend (Flask + Python)
│   ├── Routes
│   ├── Business logic
│   ├── Database access
│
├── Database (MySQL)
│
├── Infrastructure (Docker, EC2)
│
└── CI/CD (GitHub Actions)


**Project Structure**

app.py
requirement.txt
Dockerfile
docker-compose.yml
templates/index.html
.github/workflows/github-actions.yml
README.md

**How the Application Works**

Flask handles incoming HTTP requests and serves the web interface
MySQL stores application data
Flask connects to MySQL using Docker’s internal networking
Docker Compose manages the lifecycle of multiple containers
MySQL data is persisted using Docker volumes


**CI/CD Pipeline Workflow**

Code is pushed to the main branch
GitHub Actions workflow is triggered automatically
Repository source code is checked out on the runner
Pipeline connects securely to AWS EC2 using SSH
Latest code is pulled on EC2
Existing containers are stopped
Docker images are rebuilt
Containers are started using Docker Compose
Application is deployed automatically


**Application Access**

After deployment, the application is available at:
http://<EC2_PUBLIC_IP>:5000

Health check endpoint:
http://<EC2_PUBLIC_IP>:5000/health


**Key Features**

Two-tier architecture (Application + Database)
Dockerized services managed with Docker Compose
Persistent MySQL data using Docker volumes
Automated CI/CD pipeline using GitHub Actions
Health checks for application and database
Restart policies for reliability
No manual deployment after initial setup


**Security & Best Practices**

No credentials committed to source control
SSH access handled securely via GitHub Secrets
Containers communicate over an isolated Docker network
Database accessible only within the Docker network
Version-controlled CI/CD workflows
