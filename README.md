# RoseArts – E-Commerce Art Store Deployment on AWS

A web-based e-commerce art store deployed on Amazon Web Services (AWS) to showcase handmade paintings through a custom domain. This project demonstrates practical cloud deployment, networking, traffic routing, DNS configuration, and troubleshooting.

## 📌 Project Overview

**RoseArts** is a web application designed to display handmade paintings through a simple and user-friendly interface. The application was developed using Python and Flask, with HTML templates and static assets for the website.

The primary focus of this project is AWS infrastructure configuration and application deployment using Amazon EC2, Amazon VPC, an Application Load Balancer, and Amazon Route 53.

### Project Details

- **Project Name:** RoseArts – E-Commerce Art Store Deployment on AWS
- **Project Type:** Two-tier web application deployment
- **Cloud Platform:** Amazon Web Services (AWS)
- **AWS Region:** Asia Pacific (Sydney) — `ap-southeast-2`
- **Application Framework:** Python Flask
- **Application Port:** 5000
- **Domain:** `rosearts.store`
- **Deployment Environment:** Red Hat Enterprise Linux EC2 instance

## 🎯 Project Objectives

- Configure an Amazon VPC and public subnets.
- Deploy a Flask web application on Amazon EC2.
- Configure an Application Load Balancer to receive and forward HTTP traffic.
- Set up a target group and health checks for the application.
- Configure Amazon Route 53 for custom domain resolution.
- Test application accessibility and troubleshoot deployment issues.

## 🏗️ AWS Architecture

The RoseArts application is deployed within an Amazon VPC using two public subnets across two Availability Zones. A single EC2 instance hosts the application, while an Application Load Balancer provides an entry point for incoming HTTP requests. Amazon Route 53 directs the configured domain to the load balancer.

### Request Flow

**User → Amazon Route 53 → Application Load Balancer → Target Group → Amazon EC2 → RoseArts Flask Application**

### Network Configuration

| Component | Configuration |
|---|---|
| AWS Region | `ap-southeast-2` (Sydney) |
| VPC CIDR | `10.0.0.0/16` |
| Public Subnet A | `10.0.1.0/24` |
| Public Subnet B | `10.0.2.0/24` |
| EC2 Application Instance | One instance |
| ALB Listener | HTTP — Port 80 |
| Application Target Port | 5000 |
| Custom Domain | `rosearts.store` and `www.rosearts.store` |

The Application Load Balancer is configured to use two public subnets across two Availability Zones. However, the application runs on a single EC2 instance, so the deployment does not provide application-level compute redundancy.

## ☁️ AWS Services Used

### 1. Amazon VPC
Provides a logically isolated network for the project resources and supports the configuration of subnets and routing.

### 2. Amazon EC2
Hosts the RoseArts Flask application on a Red Hat Enterprise Linux instance.

### 3. Application Load Balancer (ALB)
Receives incoming HTTP requests on port 80 and forwards them to the registered target group.

### 4. Target Group
Registers the EC2 application instance and performs health checks to determine whether the target can receive traffic.

### 5. Amazon Route 53
Manages DNS records for the custom domain and directs users to the Application Load Balancer.

### 6. Security Groups
Control permitted network traffic to the load balancer and EC2 instance, including HTTP application traffic and administrative SSH access.

### 7. Internet Gateway
Provides a route between the VPC and the public internet when routing, addressing, and security configurations permit it.

## 🎨 Website Features

- **Homepage:** Introduces the RoseArts art store.
- **Paintings Gallery:** Displays the available paintings.
- **Painting Details:** Presents individual painting information.
- **Inquiry Page:** Provides an interface for painting-related inquiries.

## ⚙️ Application Deployment

The Flask application was deployed to an EC2 instance and configured to run on port 5000. The Application Load Balancer listens on port 80 and forwards requests to the application target.

The deployment workflow involved:

1. Connecting to the EC2 instance through SSH using PuTTY.
2. Navigating to the application directory.
3. Activating the Python virtual environment.
4. Starting the Flask application.
5. Checking the target group's health status.
6. Testing the website through the custom domain.

## 🧪 Testing and Validation

The deployment was validated through the following checks:

- Confirmed that the EC2 instance was running.
- Verified that the Flask application started and responded on port 5000.
- Checked the Application Load Balancer listener and target group health.
- Verified access through `rosearts.store` and `www.rosearts.store`.
- Tested the homepage, painting gallery, painting details, and inquiry page.

## 🔧 Troubleshooting

During deployment, I encountered HTTP 502 Bad Gateway and HTTP 504 Gateway Timeout errors.

### HTTP 502 Bad Gateway
Investigated the target group's health status, application process, and relevant network and security group settings during deployment troubleshooting.

### HTTP 504 Gateway Timeout
Encountered an `Address already in use` error involving port 5000. Checked the running Python process, resolved the application process conflict, and verified that the target group returned to a healthy state.

### SSH Connection Issue
Reviewed the EC2 security group's SSH inbound rule and used a restricted source IP where required to restore administrative access.

These issues provided practical experience in investigating application availability, target health, port conflicts, and SSH connectivity.

## 🔐 Security Considerations

- Restrict SSH access to a trusted source IP.
- Allow application traffic from the appropriate load balancer security group.
- Do not expose AWS access keys, passwords, private SSH keys, or other secrets in source code or repository files.
- Review security group rules before making the deployment publicly accessible.

## 💰 Cost Considerations

AWS resources may incur charges depending on their configuration and usage. Stopping the EC2 instance does not necessarily stop charges for other resources, including the load balancer and public IPv4 addresses.

Review the AWS Billing console and stop or delete resources that are no longer required.

## 📈 Future Enhancements

- Deploy additional EC2 instances across Availability Zones for application-level redundancy.
- Use private subnets for application instances with appropriate network access.
- Enable HTTPS using an appropriate TLS certificate.
- Add monitoring and alerting.
- Improve application deployment and process management.

## 📂 Repository Structure

The repository will contain the following project materials as they are reviewed and added:

```text
RoseArts-AWS-Deployment/
├── README.md
├── docs/
│   └── RoseArts_AWS_Project_Documentation.docx
├── screenshots/
├── architecture/
│   └── rosearts-architecture.png
└── application/
    └── Flask application source files
```

## 📄 Project Documentation

The detailed project report, AWS configuration screenshots, architecture diagram, and reviewed application source code will be added to this repository.

## 👩‍💻 Author

**Roselin R**

Computer Science Graduate | AWS Cloud and Networking

GitHub: [RoselinR](https://github.com/RoselinR)

---

*This project was developed for educational and demonstration purposes to gain hands-on experience with AWS cloud infrastructure, networking, application deployment, DNS configuration, and troubleshooting.*

