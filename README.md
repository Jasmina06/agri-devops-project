# 🚜 Agricultural Digital Platform - DevOps Implementation

This repository contains a full-lifecycle DevOps implementation for a digital agricultural platform. The project is designed to solve real-world agricultural challenges using automation, containerization, and cloud-native monitoring.

## 📋 Table of Contents
* [Project Overview](#project-overview)
* [Business Scenarios](#business-scenarios)
* [Tech Stack](#tech-stack)
* [CI/CD Pipeline](#cicd-pipeline)
* [Monitoring & Metrics](#monitoring--metrics)
* [Setup & Deployment](#setup--deployment)

---

## 🌟 Project Overview
The platform provides a reliable bridge between farmers and suppliers. It ensures real-time product availability and mission-critical notification systems using a robust DevOps toolchain.

## 🌾 Business Scenarios Covered
- **Scenario 1 (Product Board):** A Flask-based interface for real-time agricultural product listing and updates.
- **Scenario 2 (Notifications):** An automated system to notify suppliers of orders, with built-in reliability tracking.
- **Scenario 4 (Seasonal Demand):** Containerized architecture designed to handle peak seasonal traffic spikes.
- **Scenario 5 (Operational Visibility):** Full-stack monitoring to maintain system health and uptime.

## 🛠 Tech Stack
* **Backend:** Python (Flask)
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions
* **Cloud Infrastructure:** AWS EC2 (Ubuntu 24.04 LTS)
* **Monitoring:** Prometheus & Grafana
* **Testing:** Pytest with Coverage

---

## 🚀 CI/CD Pipeline (LO2 & LO3)
The project utilizes an automated pipeline defined in `.github/workflows/ci.yml`.

1.  **Automated Testing:** Every push triggers `pytest` to ensure functionality across all agricultural scenarios.
2.  **Continuous Deployment:** Once tests pass, the code is automatically deployed to the **AWS EC2** instance via SSH.
3.  **Security:** Deployment is secured using GitHub Secrets to manage sensitive SSH private keys.



---

## 📊 Monitoring & Metrics (LO4 & M4)
To satisfy the requirements for performance evaluation, we have integrated a real-time monitoring suite:

- **Metrics Collection:** The application exports custom Prometheus metrics via the `/metrics` endpoint.
- **Request Tracking:** Every agricultural order notification is tracked using an `http_requests_total` counter.
- **Visual Analytics:** A Grafana dashboard provides a live view of system stress levels and seasonal demand simulation.

### Evidence of Success:
- **P8 (Summarise outcomes):** The deployment on AWS (IP: 13.62.102.94) was successful, with all services running in Docker containers.
- **M4 (Analyse outcomes):** Stress tests conducted on the `/notify` endpoint showed 100% availability, as visualized in the Grafana spikes.



---

## ⚙️ Setup & Deployment

### AWS Environment Setup
The server is configured with the following open ports in the Security Group:
* `8000`: Application
* `3000`: Grafana Dashboard
* `9090`: Prometheus Server

### Running the Project Locally
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/Jasmina06/agri-devops-project.git](https://github.com/Jasmina06/agri-devops-project.git)
    ```
2.  **Start Services:**
    ```bash
    docker-compose up --build -d
    ```
3.  **Verify:**
    - App: `http://localhost:8000`
    - Metrics: `http://localhost:8000/metrics`
    - Grafana: `http://localhost:3000` (User/Pass: admin/admin)

---
**Author:** Jasmina
**Course:** BTEC Level 5 - Unit: DevOps
**Status:** Successfully Implemented & Monitored
