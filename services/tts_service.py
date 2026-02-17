import azure.cognitiveservices.speech as speechsdk
from config.settings import AZURE_KEY, AZURE_REGION
from pathlib import Path

def generate_audio(ssml: str, output_path: Path, azure_key: AZURE_KEY, azure_region: AZURE_REGION):
    """
    Generate audio file using Azure Speech TTS
    """
    speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=azure_region)
    speech_config.speech_synthesis_output_format = speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=speechsdk.audio.AudioOutputConfig(filename=str(output_path)))
    
    result = synthesizer.speak_ssml_async(ssml).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        raise RuntimeError(f"Speech synthesis failed: {result.reason}")
