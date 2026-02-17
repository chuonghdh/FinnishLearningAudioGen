from pydub import AudioSegment
from pathlib import Path
from typing import List

def merge_audio(audio_paths: List[Path], pauses_ms: List[int], output_path: Path):
    """
    Merge multiple audio files with optional pauses (in milliseconds)
    """
    final_audio = AudioSegment.silent(duration=0)

    for i, path in enumerate(audio_paths):
        audio = AudioSegment.from_file(path)
        final_audio += audio
        if i < len(pauses_ms):
            final_audio += AudioSegment.silent(duration=pauses_ms[i])

    final_audio.export(output_path, format="mp3")
