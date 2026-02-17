import streamlit as st
from pathlib import Path
import tempfile

from config.settings import AZURE_KEY, AZURE_REGION
from services.csv_loader import load_csv
from services.ssml_builder import build_ssml
from services.tts_service import generate_audio
from services.audio_utils import merge_audio

# -----------------------------
# Page Header
# -----------------------------
st.title("Generate Conversation Audio")
st.write("Upload your CSV file and generate a merged audio output.")

st.divider()

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Import CSV File",
    type=["csv"],
    accept_multiple_files=False
)

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")

st.divider()

# -----------------------------
# Generate Button
# -----------------------------
generate_clicked = st.button(
    "Generate Audio",
    type="primary",
    use_container_width=True
)

# -----------------------------
# Generate Audio Logic
# -----------------------------
if generate_clicked:
    if not uploaded_file:
        st.warning("Please upload a CSV file first.")
    else:
        st.info("Processing CSV and generating audio...")

        try:
            # 1️⃣ Load CSV rows
            rows = load_csv(uploaded_file)

            # Temporary directory for individual TTS files
            temp_dir = Path(tempfile.mkdtemp())

            audio_paths = []
            pause_ms_list = []

            # 2️⃣ Generate TTS for each row
            for idx, row in enumerate(rows):
                ssml = build_ssml(row)
                output_file = temp_dir / f"{idx:03d}.mp3"
                generate_audio(ssml, output_file, AZURE_KEY, AZURE_REGION)
                audio_paths.append(output_file)
                pause_ms_list.append(row.pause_ms)

            # 3️⃣ Merge audio segments
            final_output_path = temp_dir / "final_conversation.mp3"
            merge_audio(audio_paths, pause_ms_list, final_output_path)

            # 4️⃣ Display audio player
            st.success("Audio generated successfully!")
            with open(final_output_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.caption("Version 1.0 - Full TTS Generation")
