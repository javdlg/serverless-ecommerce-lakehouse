# Serverless E-Commerce Data Lakehouse 🏢

## 📌 Project Overview
This repository contains an end-to-end Data Engineering project designed to process and analyze the Brazilian E-Commerce Public Dataset by Olist. The architecture is built entirely on AWS using a **Serverless** and **FinOps** (cost-optimized) approach, ensuring high performance with near-zero operational costs.

## 🏗️ Architecture
The pipeline follows a modern Data Lakehouse medallion architecture (Raw -> Clean -> Business):
1. **Ingestion:** Raw CSV data is ingested into an Amazon S3 Landing Zone.
2. **Transformation:** S3 events trigger AWS Lambda functions (using AWS SDK for Pandas) to clean, cast data types, and convert files to Parquet format.
3. **Warehousing:** The optimized Parquet files are queried directly via Amazon Athena (Serverless SQL).
4. **Orchestration:** (WIP) AWS Step Functions to manage the ETL state machine.
5. **Infrastructure as Code:** The entire environment is provisioned using Terraform.

*(Note: Architecture diagram will be added in the `docs/` folder shortly).*

## 🛠️ Tech Stack
* **Cloud Provider:** AWS (S3, Lambda, Athena, IAM, Step Functions)
* **Infrastructure as Code (IaC):** Terraform
* **Language:** Python 3.x (boto3, pandas, awswrangler)
* **Data Processing:** Serverless ETL (AWS Lambda)
* **Data Warehouse / Analytics:** Amazon Athena (Presto SQL)
* **Version Control:** Git & GitHub

## 📂 Repository Structure
* `infrastructure/`: Terraform configuration files to deploy AWS resources.
* `src/`: Python source code for data extraction and Lambda transformation logic.
* `sql/`: DDL scripts for defining Athena external tables.
* `docs/`: Project documentation, architecture diagrams, and BI dashboards.

## 🚀 How to Run (Coming Soon)
Step-by-step instructions on how to configure the AWS CLI, deploy the Terraform infrastructure, and trigger the initial data load will be documented as the project progresses.

---
**Author:** Javier E. Dlogokiski, Data Science Technician.