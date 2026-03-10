# Vertex Microservices CI/CD Pipeline

## Overview

This repository contains **GitHub Actions CI/CD pipelines for the Vertex microservices platform**.

Each microservice has its own **dedicated workflow** that performs:

- Application build and testing
- Dependency vulnerability scanning
- Static code analysis
- Docker image build
- Container vulnerability scanning
- SBOM generation
- Image push to Amazon ECR

The pipelines use **GitHub OIDC authentication to securely access AWS** without storing AWS access keys.

---

# Microservices

The platform contains the following services:

```
services/
├── order-service
├── product-service
├── user-service
└── ui-service
```

Each service has a dedicated CI/CD workflow.

---

# Workflows

The repository contains the following GitHub Actions workflows:

```
.github/workflows/
├── order-service.yml
├── product-service.yml
├── ui-service.yml
└── user-service-ci.yml
```

Each workflow runs an independent CI/CD pipeline for its respective microservice.

---

# CI/CD Architecture

The CI/CD pipelines implement a **secure DevSecOps workflow**.

```
Developer
   │
   │ Push Code
   ▼
GitHub Repository
   │
   ▼
GitHub Actions Workflow
   │
   ▼
Build & Test
   │
   ▼
Security Scans
   │
   ▼
Docker Image Build
   │
   ▼
Container Scan
   │
   ▼
Authenticate with AWS (OIDC)
   │
   ▼
Push Image to Amazon ECR
```

---

# CI/CD Flow Chart

```
Code Push
   │
   ▼
GitHub Actions Trigger
   │
   ▼
Checkout Repository
   │
   ▼
Setup Java Environment
   │
   ▼
Maven Build
   │
   ▼
Unit Tests
   │
   ▼
Security Scanning
   │
   ├── OWASP Dependency Check
   ├── Semgrep SAST
   └── SonarCloud Analysis
   │
   ▼
Docker Image Build
   │
   ▼
Trivy Container Scan
   │
   ▼
Generate SBOM
   │
   ▼
Authenticate to AWS using OIDC
   │
   ▼
Push Image to Amazon ECR
```

---

# Security Tools

The pipelines include multiple security layers.

### OWASP Dependency Check

Scans application dependencies for known vulnerabilities.

---

### Semgrep

Performs **static application security testing (SAST)**.

---

### SonarCloud

Provides:

- code quality analysis
- vulnerability detection
- maintainability metrics

---

### Trivy

Scans Docker images for vulnerabilities.

The pipeline **fails if HIGH or CRITICAL vulnerabilities are detected**.

---

# AWS Authentication (OIDC)

The pipelines authenticate with AWS using **GitHub OpenID Connect (OIDC)**.

This eliminates the need for:

- AWS access keys
- long-lived credentials

Authentication flow:

```
GitHub Actions
     │
     ▼
GitHub OIDC Provider
     │
     ▼
AWS IAM Role
     │
     ▼
Temporary Credentials
     │
     ▼
Amazon ECR
```

Benefits:

- improved security
- no stored AWS secrets
- short-lived credentials
- secure AWS access

---

# Container Registry

Docker images are pushed to **Amazon Elastic Container Registry (ECR)**.

Example image format:

```
<aws-account-id>.dkr.ecr.us-west-1.amazonaws.com/vertex_ecr:<commit-sha>
```

The pipeline pushes two tags:

```
commit SHA tag
latest tag
```

---

# Technology Stack

CI/CD

- GitHub Actions

Programming Language

- Java 17

Build Tool

- Maven

Containerization

- Docker

Security Tools

- OWASP Dependency Check
- Semgrep
- SonarCloud
- Trivy

Cloud

- AWS IAM
- Amazon ECR

Authentication

- GitHub OIDC

---

# DevSecOps Features

The pipelines implement modern DevSecOps practices:

- automated CI/CD pipelines
- dependency vulnerability scanning
- static code analysis
- container vulnerability scanning
- SBOM generation
- secure AWS authentication using OIDC
- immutable container images

---

# Future Improvements

Potential improvements include:

- Kubernetes deployment pipeline
- GitOps with ArgoCD
- container image signing with Cosign
- Slack notifications
- automated deployment to EKS
