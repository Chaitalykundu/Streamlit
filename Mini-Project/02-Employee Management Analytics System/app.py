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