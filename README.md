# End-to-End ETL Pipeline for Sales Data Analysis

## Overview
A production-ready ETL (Extract, Transform, Load) pipeline built with **Apache Spark (PySpark)** and **MySQL**. This project simulates a real-world data engineering task by ingesting raw, messy sales data, applying robust data cleaning and transformations, and loading it into a structured data warehouse for analysis. It showcases core competencies in data processing, database management, and automation.

## Architecture
```mermaid
graph LR
    A[Raw Data<br>CSV/JSON] --> B[Extract<br>Python]
    B --> C[Transform<br>PySpark]
    C --> D[Load<br>MySQL Connector]
    D --> E[MySQL Data Warehouse]
