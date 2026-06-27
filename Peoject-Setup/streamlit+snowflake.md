# Streamlit + Snowflake Integration Guide

## Table of Contents

- [Streamlit + Snowflake Integration Guide](#streamlit--snowflake-integration-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Step 1 — Install Python](#step-1--install-python)
  - [Step 2 — Create Project Folder](#step-2--create-project-folder)
  - [Step 3 — Create and Activate Virtual Environment](#step-3--create-and-activate-virtual-environment)
  - [Step 4 — Install Required Packages](#step-4--install-required-packages)
  - [Step 5 — Create Snowflake Environment](#step-5--create-snowflake-environment)
  - [Step 6 — Design Your Database](#step-6--design-your-database)
  - [Step 7 — Recommended Project Structure](#step-7--recommended-project-structure)
  - [Step 8 — Build the Snowflake Connection](#step-8--build-the-snowflake-connection)
  - [Step 9 — Configure Environment Variables](#step-9--configure-environment-variables)
    - [9.1 Create `.env` File](#91-create-env-file)
    - [9.2 Finding Your Snowflake Account ID](#92-finding-your-snowflake-account-id)
    - [9.3 Add `.env` to `.gitignore`](#93-add-env-to-gitignore)
  - [Step 10 — Test Connection](#step-10--test-connection)
  - [Troubleshooting](#troubleshooting)
    - [Error: `ModuleNotFoundError: No module named 'snowflake_connection'`](#error-modulenotfounderror-no-module-named-snowflake_connection)
    - [Error: `Missing environment variables: USER, PASSWORD, etc.`](#error-missing-environment-variables-user-password-etc)
    - [Error: `404 Not Found: post xyz.snowflakecomputing.com:443/session/v1/login-request`](#error-404-not-found-post-xyzsnowflakecomputingcom443sessionv1login-request)
    - [Error: `NoneType object has no attribute 'find'`](#error-nonetype-object-has-no-attribute-find)
    - [Error: `Invalid username, password, or account identifier`](#error-invalid-username-password-or-account-identifier)
    - [Connection is slow](#connection-is-slow)
  - [Best Practices](#best-practices)

---

## Overview

This guide will walk you through setting up a complete Streamlit application integrated with Snowflake Data Warehouse. We'll cover environment setup, database design, connection management, and testing.

**Key Requirements:**

- Python 3.8+
- Snowflake Account
- Pip package manager

---

## Step 1 — Install Python

Check your Python version:

```bash
python --version
```

Ensure you have Python 3.8 or higher installed.

---

## Step 2 — Create Project Folder

```bash
mkdir employee_analytics_system
cd employee_analytics_system
```

---

## Step 3 — Create and Activate Virtual Environment

**For Windows (PowerShell):**

```bash
python -m venv env
& env\Scripts\Activate.ps1
```

**For macOS/Linux:**

```bash
python -m venv env
source env/bin/activate
```

---

## Step 4 — Install Required Packages

Install all required dependencies:

```bash
pip install streamlit
pip install snowflake-connector-python
pip install python-dotenv
pip install pandas
pip install plotly
pip install faker
```

**Create requirements.txt:**

```bash
pip freeze > requirements.txt
```

**Or manually create requirements.txt:**

```
streamlit==1.28.0
snowflake-connector-python==3.4.0
python-dotenv==1.0.0
pandas==2.0.0
plotly==5.17.0
faker==20.1.0
```

---

## Step 5 — Create Snowflake Environment

In your Snowflake account, create the following:

1. **Database**: `Employee_Management_Analytics_System`
2. **Schema**: `Analytics_System`
3. **Warehouse**: `COMPUTE_WH`
4. **Role**: `ACCOUNTADMIN` (or create a custom role)

You can do this via the Snowflake UI or run SQL commands in the Query Editor.

---

## Step 6 — Design Your Database

**⚠️ IMPORTANT:** Design your database BEFORE coding UI.

Consider the following:

- **Fact Tables**: Tables containing measurable events (e.g., sales, employee records)
- **Dimension Tables**: Tables containing descriptive attributes (e.g., employees, departments)
- **Indexes**: Plan for query optimization
- **Data Types**: Choose appropriate data types for each column

Example dimension table:

```sql
CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    DEPARTMENT VARCHAR(50),
    HIRE_DATE DATE,
    SALARY NUMBER(10, 2)
);
```

---

## Step 7 — Recommended Project Structure

```
employee_analytics_system/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (DO NOT COMMIT)
├── .gitignore                  # Git ignore file
│
├── snowflake_connection.py     # Snowflake connection module
│
├── pages/                      # Streamlit multi-page apps
│   ├── dashboard.py
│   ├── reports.py
│   └── settings.py
│
├── database/
│   ├── schema.sql              # Database schema definitions
│   ├── seed_data.py            # Sample data initialization
│   └── queries.py              # Reusable SQL queries
│
├── utils/
│   ├── charts.py               # Chart/visualization helpers
│   ├── data_processing.py      # Data manipulation functions
│   └── helpers.py              # General utility functions
│
└── assets/                     # Images, logos, etc.
```

---

## Step 8 — Build the Snowflake Connection

Create a `snowflake_connection.py` file in your project root:

```python
"""
Snowflake Connection Module

Handles secure connection to Snowflake Data Warehouse.
Credentials are loaded from .env file for security.
"""

import os
from dotenv import load_dotenv
import snowflake.connector

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, override=True)

def create_connection():
    """
    Establishes a secure connection to Snowflake.

    Returns:
        snowflake.connector.connection.SnowflakeConnection

    Raises:
        ValueError: If required environment variables are missing
        snowflake.connector.errors.DatabaseError: If connection fails
    """

    # Retrieve credentials from environment variables
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    account = os.getenv("ACCOUNT")
    warehouse = os.getenv("WAREHOUSE")
    database = os.getenv("DATABASE")
    schema = os.getenv("SCHEMA")
    role = os.getenv("ROLE")

    # Validate all required variables are present
    required_vars = {
        "USER": user,
        "PASSWORD": password,
        "ACCOUNT": account,
        "WAREHOUSE": warehouse,
        "DATABASE": database,
        "SCHEMA": schema,
        "ROLE": role
    }

    missing = [key for key, value in required_vars.items() if not value]
    if missing:
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")

    # Create and return Snowflake connection
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role
    )

    return conn
```

---

## Step 9 — Configure Environment Variables

### 9.1 Create `.env` File

Create a `.env` file in your project root (same level as `app.py`):

```env
USER=your_snowflake_username
PASSWORD=your_snowflake_password
ACCOUNT=your_account_id.region.cloud_provider
WAREHOUSE=COMPUTE_WH
DATABASE=Employee_Management_Analytics_System
SCHEMA=Analytics_System
ROLE=ACCOUNTADMIN
```

### 9.2 Finding Your Snowflake Account ID

1. Log in to Snowflake: https://www.snowflake.com/
2. Look at the URL in your browser: `https://app.snowflake.com/region/account_id/`
3. Your account ID format: `account_id.region.provider` (e.g., `lk834585.ap-southeast-7.aws`)

### 9.3 Add `.env` to `.gitignore`

Create or update `.gitignore` in your project root:

```
# Environment variables
.env
.env.local
.env.*.local

# Virtual environment
env/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# IDE
.vscode/
.idea/
*.swp
*.swo

# Streamlit
.streamlit/
```

**⚠️ IMPORTANT:** Never commit your `.env` file to version control!

---

## Step 10 — Test Connection

Create a simple test in `app.py` or a dedicated test file:

```python
import streamlit as st
import pandas as pd
from snowflake_connection import create_connection

st.set_page_config(page_title="Snowflake Test", layout="wide")
st.title("🔗 Snowflake Connection Test")

try:
    conn = create_connection()

    # Test query
    query = "SELECT CURRENT_VERSION()"
    df = pd.read_sql(query, conn)

    st.success("✅ Connection Successful!")
    st.write("**Snowflake Version:**")
    st.dataframe(df)

    conn.close()

except ValueError as e:
    st.error(f"❌ Configuration Error: {e}")
    st.info("Please check your .env file has all required variables.")

except Exception as e:
    st.error(f"❌ Connection Failed: {e}")
    st.info("Please verify your credentials and account ID.")
```

**Run the test:**

```bash
streamlit run app.py
```

---

&nbsp;

&nbsp;

## Troubleshooting

### Error: `ModuleNotFoundError: No module named 'snowflake_connection'`

**Solution:**

- Ensure `snowflake_connection.py` is in your project root directory
- Check file naming: should use underscore `_`, not hyphen `-`

&nbsp;

### Error: `Missing environment variables: USER, PASSWORD, etc.`

**Solution:**

- Verify `.env` file exists in project root
- Check .env file format: `KEY=VALUE` (no spaces around `=`)
- Restart your Streamlit app after creating/modifying .env

&nbsp;

### Error: `404 Not Found: post xyz.snowflakecomputing.com:443/session/v1/login-request`

**Solution:**

- Incorrect account ID format
- Verify your Snowflake URL: `https://app.snowflake.com/region/account_id/`
- Account format should be: `account_id` or `account_id.region.provider`
- Example: `lk834585.ap-southeast-7.aws`

&nbsp;

### Error: `NoneType object has no attribute 'find'`

**Solution:**

- .env file not loading properly
- Use `override=True` in `load_dotenv()` to override system variables
- Ensure USER, PASSWORD variables are not None

&nbsp;

### Error: `Invalid username, password, or account identifier`

**Solution:**

- Verify Snowflake username and password are correct
- Try logging into Snowflake directly: https://www.snowflake.com/
- Ensure account is not suspended
- Check role has proper permissions

### Connection is slow

**Solution:**

- Use connection pooling for multiple queries
- Optimize SQL queries with proper indexes
- Use Streamlit caching with `@st.cache_resource`

---

&nbsp;

&nbsp;

## Best Practices

1. **Security**
   - Never hardcode credentials
   - Always use `.env` files
   - Add `.env` to `.gitignore`
   - Use environment-specific credentials

2. **Performance**
   - Use Streamlit caching decorators
   - Limit data returned from queries
   - Use warehouse sizing appropriate for workload

3. **Development**
   - Test connection before building UI
   - Use version control (Git)
   - Document your database schema
   - Create seed data for testing

4. **Deployment**
   - Use production-grade database credentials
   - Enable query monitoring
   - Set up proper backup strategies
   - Use read-only roles for analytics
