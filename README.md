# Cloud Resume Project 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
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
```
 




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
```

## Features

### Frontend



* HTML/CSS/JS static site
* Responsive design suitable for desktop and mobile
* Visitor counter calls the Lambda API to track visits
* Cache headers set to optimize CloudFront performance


---

### Backend



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
  * Lambda full access
  * DynamoDB full access
  * CloudFront full access
  * Route 53 full access
* AWS CLI installed and configured
* SAM CLI installed
* GitHub account for CI/CD

## Steps
1. Clone the repo

```bash
   git clone https://github.com/YOUR_USERNAME/resume-website.git
   cd resume-website
```

2. Deploy infrastructure with SAM
```bash
   cd infrastructure
   sam build
   sam deploy --guided
```
 

3. Upload frontend to S3


   This is handled automatically by CI/CD, but you can also manually sync:

```bash
   aws s3 sync ../frontend/ s3://YOUR_BUCKET_NAME --delete
```
4. Invalidate CloudFront cache

```bash 
   aws cloudfront create-invalidation --distribution-id YOUR_CLOUDFRONT_ID --paths "/*"
```

5. Verify site

   Open your browser at your custom domain with HTTPS:

```bash
   https://yourdomain.com
```

## CI/CD with GitHub Actions
 * Workflow triggers on push to main branch
 * Automatically deploys backend (Lambda + DynamoDB) and frontend (S3 + CloudFront)
 * Invalidates CloudFront cache so updates appear immediately

## Logging & Monitoring
 * Structured JSON logs for every visitor increment
 * CloudWatch metrics track visitor increments
 * Alarms can be configured for error detection or unusual traffic

## Future Enhancements
 * X-Ray tracing for full request tracking across Lambda and API Gateway
 * Optional analytics dashboard using CloudWatch Metrics + Logs Insights
 * Additional frontend features: resume download, portfolio links

## Skills Demonstrated
 * AWS serverless architecture (Lambda, DynamoDB, API Gateway, S3, CloudFront, Route 53)
 * CI/CD pipelines (GitHub Actions)
 * Python backend development
 * Frontend web development (HTML/CSS/JS)
 * Structured logging, monitoring, and observability
 * Performance optimization via caching headers and CDN
 * Production-ready deployment workflows

## LICENSE
MIT License © B. FAKO