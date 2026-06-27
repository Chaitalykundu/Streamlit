"""
Snowflake Connection Module
============================

This module handles the creation and management of connections to Snowflake Data Warehouse.
It loads credentials from environment variables defined in a .env file and establishes
a secure connection to the Snowflake account.

CONFIGURATION:
The following environment variables must be defined in a .env file in the project root:

    USER          : Snowflake username
    PASSWORD      : Snowflake password
    ACCOUNT       : Snowflake account ID (e.g., lk227585.ap-southeast-7.aws)
    WAREHOUSE     : Snowflake warehouse name (e.g., COMPUTE_WH)
    DATABASE      : Snowflake database name (e.g., Employee_Management_Analytics_System)
    SCHEMA        : Snowflake schema name (e.g., Analytics_System)
    ROLE          : Snowflake role name (e.g., ACCOUNTADMIN)

USAGE EXAMPLE:
    from snowflake_connection import create_connection
    import pandas as pd

    conn = create_connection()
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, conn)
    conn.close()

NOTES:
    - Ensure the .env file exists in the project root directory
    - Keep your credentials secure and never commit .env to version control
    - Add .env to your .gitignore file
"""

import os
from dotenv import load_dotenv
import snowflake.connector

# Load .env file from project root
# The override=True parameter ensures .env variables take precedence over system variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, override=True)


def create_connection():
    """
    Establishes a connection to Snowflake Data Warehouse.

    This function reads Snowflake credentials from environment variables and creates
    a secure connector to the specified Snowflake account, warehouse, database, and schema.

    Returns:
        snowflake.connector.connection.SnowflakeConnection
            A connection object that can be used to execute queries

    Raises:
        ValueError: If any required environment variable is missing
        snowflake.connector.errors.DatabaseError: If connection fails due to
            invalid credentials or account issues

    Environment Variables Required:
        USER       : Snowflake username
        PASSWORD   : Snowflake password
        ACCOUNT    : Snowflake account identifier (e.g., xy12345.region.provider)
        WAREHOUSE  : Name of the warehouse to use
        DATABASE   : Default database for the connection
        SCHEMA     : Default schema within the database
        ROLE       : Role to use for this connection

    Example:
        >>> conn = create_connection()
        >>> cursor = conn.cursor()
        >>> cursor.execute("SELECT CURRENT_VERSION()")
        >>> result = cursor.fetchall()
        >>> conn.close()
    """

    # Retrieve credentials from environment variables
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    account = os.getenv("ACCOUNT")
    warehouse = os.getenv("WAREHOUSE")
    database = os.getenv("DATABASE")
    schema = os.getenv("SCHEMA")
    role = os.getenv("ROLE")

    # Validate that all required variables are present
    if not all([user, password, account, warehouse, database, schema, role]):
        missing = []
        if not user: missing.append("USER")
        if not password: missing.append("PASSWORD")
        if not account: missing.append("ACCOUNT")
        if not warehouse: missing.append("WAREHOUSE")
        if not database: missing.append("DATABASE")
        if not schema: missing.append("SCHEMA")
        if not role: missing.append("ROLE")
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")

    # Establish connection to Snowflake
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