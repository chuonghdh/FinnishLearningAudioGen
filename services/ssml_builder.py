from models.row_model import SentenceRow

def build_ssml(row: SentenceRow) -> str:
    """
    Convert a SentenceRow into Azure Speech SSML format
    """
    # Example with emotion and speaking rate
    ssml = f"""
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='{row.language}'>
    <voice name='{row.voice}'>
        <express-as type='{row.emotion}'>
            <prosody rate='{row.speed}'>
                {row.sentence}
            </prosody>
        </express-as>
    </voice>
</speak>
"""
    return ssml.strip()
