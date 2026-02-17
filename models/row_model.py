from dataclasses import dataclass

@dataclass
class SentenceRow:
    sentence: str
    language: str
    voice: str
    emotion: str
    speed: float
    pause_ms: int