import streamlit as st

# -----------------------------
# Global Page Config
# -----------------------------
st.set_page_config(
    page_title="AI TTS Generator",
    page_icon="🔊",
    layout="centered"
)

# -----------------------------
# Landing Page
# -----------------------------
st.title("AI Text-to-Speech Generator")
st.write(
    """
Welcome 👋

Use the **left sidebar** to navigate.

Start with **Generate Audio** to upload a CSV file and create speech audio.
"""
)

st.divider()

st.caption("Version 1.0 - MVP")
