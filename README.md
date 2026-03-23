# Cloud Resume Project 

## Overview

This project is a **fully serverless, cloud-hosted personal resume website**. It demonstrates a full-stack AWS serverless architecture, including:

- **Static website hosting** on Amazon S3  
- **Global CDN and HTTPS** via Amazon CloudFront  
- **Custom domain** managed with Route 53  
- **Visitor counter** powered by AWS Lambda, DynamoDB, and API Gateway  
- **Structured logging and monitoring** via CloudWatch  
- **CI/CD pipeline** with GitHub Actions for automated deployment

This project is designed to showcase modern cloud architecture skills, including **serverless development, infrastructure as code (SAM), performance optimization, and production-grade monitoring**.

---

## Architecture

```text 
User Browser
   │
   ▼
Custom Domain (Route 53)
   │
   ▼
CloudFront Distribution (HTTPS)
   │
   ▼
S3 Bucket (Static Website)
   │
   ▼
JavaScript Visitor Counter → API Gateway → Lambda
   │
   ▼
DynamoDB Table (Visitor Count)
   │
   ▼
CloudWatch Logs & Metrics

---

### Key features:

* Global, fast website delivery with caching headers via CloudFront
* Serverless backend tracking visitor counts
* Structured JSON logging for traceable requests
* Automated CI/CD pipeline that updates frontend, backend, and invalidates CloudFront cache

## Folder Structure

```text
resume-website/
│
├── frontend/
│   ├── index.html          # Resume HTML
│   ├── styles/
│   │   └── main.css        # CSS styling
│   ├── scripts/
│   │   └── visitor.js      # JS visitor counter logic
│   └── assets/
│       └── images/         # Profile image, icons, etc.
│
├── backend/
│   └── visitor_counter/
│       ├── app.py          # Lambda handler (Python)
│       ├── requirements.txt
│       └── tests/
│           ├── test_app.py # Unit tests
│           └── __init__.py
│
├── infrastructure/
│   └── template.yaml       # AWS SAM template (infrastructure as code)
│
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions CI/CD workflow
├── samconfig.toml          # SAM CLI deployment config
├── README.md               # Project documentation
└── .gitignore

## Features

### Frontend

```text

* HTML/CSS/JS static site
* Responsive design suitable for desktop and mobile
* Visitor counter calls the Lambda API to track visits
* Cache headers set to optimize CloudFront performance

---

### Backend

```text

* AWS Lambda written in Python
* Uses DynamoDB to store visitor counts
* Structured JSON logging via CloudWatch
* Custom CloudWatch metrics for monitoring site usage
* Unit tests with pytest

## Infrastructure 

* Defined via AWS SAM template
* Deploys Lambda, DynamoDB table, and API Gateway endpoint
* Fully serverless and scalable

## CI/CD
* GitHub Actions workflow triggers on push to main branch
* Automatically:
 * Builds and deploys Lambda (SAM)
 * Uploads frontend to S3
 * Invalidates CloudFront cache

## Deployment

### Prerequisites
* AWS account with IAM user having:
 * S3 full access
Lambda full access
DynamoDB full access
CloudFront full access
Route 53 full access
AWS CLI installed and configured
SAM CLI installed
GitHub account for CI/CD