Two Tier Flask Application with Docker and Automated CI/CD Using GitHub Actions on AWS

Author: Saksham Saxena
Date: December 24, 2025

This project demonstrates a production-style two-tier web application built using Flask and MySQL, containerized with Docker, orchestrated using Docker Compose, and deployed automatically to AWS EC2 through a GitHub Actions CI/CD pipeline.

The primary objective of this project is to showcase real-world DevOps practices, including containerization, automation, and cloud deployment.


Architecture Overview:


    Developer Push (main)
            |
            v
    GitHub Actions (CI/CD)
            |
            v
    AWS EC2 (Ubuntu)
            |
            v
    Docker Compose
    ├── Flask Application (Port 5000)
    └── MySQL Database (Persistent Volume)


Tools & Technologies Used:

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


## Project Structure

.
├── app.py
├── requirement.txt
├── Dockerfile
├── docker-compose.yml
├── templates/
│   └── index.html
├── .github/
│   └── workflows/
│       └── github-actions.yml
└── README.md


How the Application Works:

    1. Flask handles incoming HTTP requests and serves the web interface

    2. MySQL stores application data

    3. Flask connects to MySQL using Docker’s internal networking

    4. Docker Compose manages the lifecycle of multiple containers

    5. MySQL data is persisted using Docker volumes


CI/CD Pipeline Workflow:

    1. Code is pushed to the main branch

    2. GitHub Actions workflow is triggered automatically

    3. Repository source code is checked out on the runner

    4. Pipeline connects securely to AWS EC2 using SSH

    5. Latest code is pulled on EC2

    6. Existing containers are stopped

    7. Docker images are rebuilt

    8. Containers are started using Docker Compose

    9. Application is deployed automatically


Application Access:

    After deployment, the application is available at:
    http://<EC2_PUBLIC_IP>:5000

    Health check endpoint:
    http://<EC2_PUBLIC_IP>:5000/health


Key Features:

    1. Two-tier architecture (Application + Database)

    2. Dockerized services managed with Docker Compose

    3. Persistent MySQL data using Docker volumes

    4. Automated CI/CD pipeline using GitHub Actions

    5. Health checks for application and database

    6. Restart policies for reliability

    7. No manual deployment after initial setup


Security & Best Practices:

    1. No credentials committed to source control

    2. SSH access handled securely via GitHub Secrets

    3. Containers communicate over an isolated Docker network

    4. Database accessible only within the Docker network

    5. Version-controlled CI/CD workflows