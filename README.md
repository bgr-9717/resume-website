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