from pathlib import Path
import os

# -----------------------------
# Detect Streamlit Cloud environment
# -----------------------------
# Streamlit sets an env variable in the cloud
USING_STREAMLIT_CLOUD = os.getenv("STREAMLIT_SERVER_RUN") == "true"

if USING_STREAMLIT_CLOUD:
    # Safe import of streamlit only in cloud
    import streamlit as st
    AZURE_KEY = st.secrets.get("AZURE_KEY")
    AZURE_REGION = st.secrets.get("AZURE_REGION")
else:
    # Local dev using .env
    from dotenv import load_dotenv

    # Load .env from project root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)

    AZURE_KEY = os.getenv("AZURE_KEY")
    AZURE_REGION = os.getenv("AZURE_REGION")

# -----------------------------
# Validate keys
# -----------------------------
if not AZURE_KEY or not AZURE_REGION:
    raise ValueError(
        "Azure Speech key or region not found!\n"
        "In dev: create a .env file with AZURE_KEY and AZURE_REGION\n"
        "In Streamlit Cloud: set them in st.secrets"
    )
