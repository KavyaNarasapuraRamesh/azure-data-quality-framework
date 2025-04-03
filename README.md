
# Azure Data Quality Monitoring Framework

A fully automated, end-to-end data quality monitoring framework built using Microsoft Azure cloud services. This system handles data profiling, rule-based validation, remediation, and reporting using an enterprise-ready architecture.

## 🔍 Overview

This project provides a scalable, cloud-native solution for monitoring, validating, and improving data quality across diverse datasets. It uses Azure Databricks for processing, Data Factory for orchestration, Blob Storage for data lifecycle management, Azure SQL Database for quality metrics storage, and Power BI for visualization.

> ✅ **Achieved Data Cleanliness Score**: 91.09%  
> 📊 **Dashboards**: Executive, Rule Violations, and Column Quality  
> ⚙️ **Pipeline**: Event-triggered, parameterized, and modular  
> 🔐 **Note**: Secrets and credentials are redacted for public sharing

## 📁 Project Structure

.
├── Notebooks/                     # PySpark notebooks for profiling, validation, remediation
├── data_factory_pipeline/         # JSON exports of ADF pipeline and trigger
├── blob_structure/                # Folder structure representing containers in Azure Blob
├── sql_scripts/                   # SQL table schemas
├── Power BI Dashboards/           # .pbix file(s) for visual reporting
└── README.md                      # This file

## ☁️ Architecture

### 🔸 Storage Layer
- **Azure Blob Storage** with containers:
  - `raw-data/` – Incoming unprocessed data
  - `profiled-data/` – Post-profiling metadata-enriched datasets
  - `remediated-data/` – Data after quality fixes
  - `certified-data/` – Final certified datasets

### 🔸 Processing Layer
- **Azure Databricks** (PySpark):
  - `Data Profiling`
  - `Rules Engine`
  - `Remediation Engine`
  - `Validation Engine`

### 🔸 Orchestration Layer
- **Azure Data Factory**:
  - Event-based pipeline with blob trigger
  - Executes Databricks notebooks with parameters

### 🔸 Persistence Layer
- **Azure SQL Database**:
  - Tables: `DataQualityMetrics`, `Profiles`, `Issues`, `Rules`, `Validation`, `DatasetMetadata`

### 🔸 Visualization Layer
- **Power BI**:
  - Executive Dashboard
  - Rules & Violations Dashboard
  - Column Quality Dashboard

## 🛠️ Tech Stack

| Service         | Usage                                  |
|----------------|------------------------------------------|
| Azure Databricks | PySpark-based data processing          |
| Azure Data Factory | Pipeline orchestration with blob triggers |
| Azure Blob Storage | Raw, processed, remediated, and certified data |
| Azure SQL Database | Stores profiling and validation metrics |
| Power BI         | Real-time dashboarding and reporting   |
| GitHub           | Version control for notebooks, pipelines, scripts |

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/KavyaNarasapuraRamesh/azure-data-quality-framework.git
cd azure-data-quality-framework
```

### 2. Set up Azure Resources
- Create an Azure Resource Group
- Provision:
  - Azure Storage Account (create containers)
  - Azure SQL Database (execute table creation scripts)
  - Azure Databricks workspace
  - Azure Data Factory (import JSON pipeline)

### 3. Upload Data
Upload dirty CSV files to the `raw-data/` container. Ensure filenames end with `_dirty.csv`.

### 4. Trigger Pipeline
Blob trigger automatically initiates ADF pipeline:
- Executes notebooks
- Populates SQL Database
- Updates Power BI dashboards

## 🔐 Security Notice

For public sharing:
- All hardcoded credentials have been removed
- Encrypted credentials in ADF linked services are **redacted**
- Power BI .pbix files do not contain connection strings

Make sure to **use Azure Key Vault** for secrets in production environments.

## 📊 Sample Dashboards

- **Executive Dashboard** – Overview of cleanliness scores and remediation status  
- **Rules & Violations Dashboard** – Insights on violated rules and severity  
- **Column Quality Dashboard** – Null count, distinct values, completeness by column

> 📁 Check `Power BI Dashboards/` for `.pbix` files

## 🧠 Future Enhancements

- 🔍 ML-based anomaly detection
- 📈 Longitudinal quality trend tracking
- 🚨 Alerts on rule violations or pipeline failures
- 🌐 Support for more file types (e.g., Parquet, Delta)
- 🗂 Integration with Azure Purview for metadata cataloging

## 🧾 References

- [Databricks Workflows](https://docs.databricks.com/aws/en/notebooks/notebook-workflows)
- [Microsoft Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)
- [Data Governance Insights](https://www.microsoft.com/en-us/security/business/security-101/what-is-data-governance-for-enterprise)

## 👩‍💻 Author

**Kavya Narasapura Ramesh**  
Department of EECS, University of Toledo  
📧 kavya.nramesh@gmail.com

## ⭐ Star this repo if you found it useful!
