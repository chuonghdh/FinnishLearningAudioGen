import pandas as pd
from pathlib import Path
from typing import List
from models.row_model import SentenceRow

REQUIRED_COLUMNS = ["sentence", "language", "voice", "emotion", "speed", "pause_ms"]

def load_csv(file_path: Path) -> List[SentenceRow]:
    """
    Load CSV file and return a list of SentenceRow dataclasses
    """
    df = pd.read_csv(file_path)

    # Check columns
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"CSV is missing required columns: {missing}")

    # Convert rows to SentenceRow
    rows = []
    for _, row in df.iterrows():
        rows.append(
            SentenceRow(
                sentence=row["sentence"],
                language=row["language"],
                voice=row["voice"],
                emotion=row["emotion"],
                speed=float(row["speed"]),
                pause_ms=int(row["pause_ms"])
            )
        )

    return rows
