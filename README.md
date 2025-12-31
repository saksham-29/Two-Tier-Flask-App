## Two-Tier Flask Application
---

Two-tier Flask web application deployed on AWS EC2 using Docker and NGINX, secured with HTTPS, with CI/CD automation implemented using GitHub Actions.

> **Important Notes**
>
> * `Dockerfile` and `docker-compose.yml` are located inside the **`docker/` directory**
> * Application source code resides in **`src/`**
> * **NGINX and HTTPS configuration on EC2 are currently not included in the repository** but are documented below for deployment reference

---

## Architecture Overview

```
Client (Browser)
      |
   HTTPS (443)
      |
   NGINX (EC2 Host)
      |
 Docker Network
 ┌───────────────┐        ┌───────────────┐
 | Flask App     | <----> | MySQL DB       |
 | (Container)   |        | (Container)   |
 └───────────────┘        └───────────────┘
```

---

## Technology Stack

* **Backend:** Flask (Python)
* **Templates:** Jinja2 (`templates/index.html`)
* **Database:** MySQL
* **Containerization:** Docker
* **Orchestration:** Docker Compose
* **Reverse Proxy (Production):** NGINX
* **Security:** HTTPS (Let’s Encrypt / Certbot)
* **Cloud:** AWS EC2
* **CI/CD:** GitHub Actions

---

## Project Structure

```
.
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── src/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── message.sql
└── README.md
```

---

## Prerequisites

### Local Development

* Docker
* Docker Compose
* Git

### Production (EC2)

* Ubuntu EC2 instance
* Security group ports open:

  * `22` – SSH
  * `80` – HTTP
  * `443` – HTTPS
* Domain name (recommended for HTTPS)

---

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saksham-29/Two-Tier-Flask-App.git
cd Two-Tier-Flask-App
```

### 2. Build and Run Containers

```bash
cd docker
docker compose up --build -d
```

### 3. Access the Application

```text
http://localhost:5000
```

The Flask app renders `templates/index.html` using Jinja2.

---

## Application Details

### Flask Application

* Entry point: `src/app.py`
* Dependencies: `src/requirements.txt`
* HTML Templates: `src/templates/index.html`

Flask runs inside a Docker container and communicates with MySQL using the Docker network defined in `docker-compose.yml`.

---

## Database

* MySQL runs as a separate Docker container
* Database schema is provided in:

```text
message.sql
```

This file initializes required tables for the application.

---

## EC2 Deployment (Docker Compose + NGINX + HTTPS)

> The following steps describe the **production setup**.
> These configurations are **not yet committed** to the repository.

---

### EC2 Setup

```bash
sudo apt update
sudo apt install -y docker.io docker-compose git
sudo systemctl enable docker
sudo systemctl start docker
```

Clone and start the application:

```bash
git clone https://github.com/saksham-29/Two-Tier-Flask-App.git
cd Two-Tier-Flask-App/docker
docker compose up --build -d
```

---

## NGINX Reverse Proxy (Production)

NGINX runs on the **EC2 host** and forwards traffic to the Flask container.

### Sample NGINX Configuration

```nginx
server {
    listen 80;
    server_name YOUR_DOMAIN_OR_EC2_IP;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## HTTPS (TLS) with Let’s Encrypt

Install Certbot:

```bash
sudo apt install certbot python3-certbot-nginx
```

Generate SSL certificates:

```bash
sudo certbot --nginx \
  --non-interactive \
  --agree-tos \
  -m your-email@example.com \
  -d yourdomain.com
```

Certbot will:

* Enable HTTPS
* Redirect HTTP → HTTPS
* Auto-renew certificates

---


## Environment Variables

Environment variables are defined in `docker/docker-compose.yml`.

Example:

```env
MYSQL_ROOT_PASSWORD=securepassword
MYSQL_DATABASE=flaskdb
```

For production:

* Use `.env` (excluded via `.gitignore`)
* Or AWS Secrets Manager (recommended)

---
