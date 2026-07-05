# Electronics Pricing Warehouse

A modern ELT pipeline that extracts Google Shopping data from SerpAPI, stores it in DuckDB, and transforms it using dbt into analytics-ready models.

The project demonstrates a complete data engineering workflow, including data extraction, storage, transformation, testing, incremental models, snapshots, and dimensional modeling.
![Uploading image.png…]()

---

# Architecture

```
SerpAPI
    │
    ▼
Raw JSON
    │
    ▼
Parquet Files
    │
    ▼
DuckDB
    │
    ▼
dbt
 ├── Staging
 ├── Intermediate
 └── Marts
      ├── Star Schema
      └── Flat Reporting Mart
```

---

# Features

- Google Shopping extraction using SerpAPI
- JSON → Parquet conversion
- Local analytical warehouse with DuckDB
- ELT transformations using dbt
- Incremental fact models
- dbt snapshots for historical tracking
- Data quality testing using dbt
- Star schema and flat reporting mart
- Python orchestration scripts

---

# Repository Structure

```text
electronics_pricing_warehouse/

├── 01_api_extraction.py
├── 02_dataframe_creation.py
├── 03_load_to_duckdb.py
├── 04_master_build.py
├── 05_run_snapshots.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── warehouse/
│       └── pricing.duckdb
│
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
│
├── snapshots/
├── dbt_project.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- DuckDB
- dbt
- SerpAPI

---

# Getting Started

## Prerequisites

- Python 3.11+
- dbt Core
- dbt-duckdb
- DuckDB
- SerpAPI API Key

---

## Installation

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Install dbt.

```bash
pip install dbt-core dbt-duckdb
```

---

## Configure dbt

Example `profiles.yml`

```yaml
outputs:
  dev:
    type: duckdb
    path: data/warehouse/pricing.duckdb
```

---

## Configure SerpAPI

Windows

```powershell
set SERPAPI_KEY=your_api_key
```

Linux / macOS

```bash
export SERPAPI_KEY=your_api_key
```

---

# Running the Pipeline

## Manual Execution

```bash
python 01_api_extraction.py
python 02_dataframe_creation.py
python 03_load_to_duckdb.py
```

---

## Run dbt

Build models.

```bash
dbt build --exclude resource_type:snapshot
```

Run tests.

```bash
dbt test
```

Run snapshots.

```bash
dbt snapshot
```

---

## Orchestration

Run the complete ELT pipeline.

```bash
python 04_master_build.py
```

Run snapshots separately.

```bash
python 05_run_snapshots.py
```

---

# dbt Project Structure

```
models/
├── staging/
├── intermediate/
└── marts/
    ├── core/
    │   ├── dim_product
    │   ├── dim_source
    │   ├── dim_date
    │   └── fct_product_listings
    │
    └── reporting/
        └── mart_shopping_flat
```

---

# Data Quality

The project uses dbt tests to validate data integrity.

Implemented tests include:

- not_null
- unique
- accepted_values
- relationships

---

# Materialization Strategy

| Layer | Materialization |
|---------|----------------|
| Staging | View |
| Intermediate | View |
| Dimensions | Table |
| Fact | Incremental |
| Reporting Mart | Table |

---

# Scheduling

Recommended schedule:

| Task | Frequency |
|------|-----------|
| 04_master_build.py | Hourly |
| 05_run_snapshots.py | Daily |

Production orchestration can be handled with:

- Apache Airflow
- Prefect
- GitHub Actions
- Windows Task Scheduler
- Cron

---

# Troubleshooting

### DuckDB database is locked

Close any open DuckDB sessions before running dbt.

---

### dbt cannot find a column

Rebuild upstream models and remove compiled artifacts if necessary.

```bash
dbt clean
```

or delete

```
target/
dbt_packages/
```

---

### dbt command not found

Ensure dbt is installed inside the active virtual environment.

---

# License

This project is licensed under the MIT License.
