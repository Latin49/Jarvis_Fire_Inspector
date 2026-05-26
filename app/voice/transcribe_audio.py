from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def transcribe_audio(file_path: str):

    with open(file_path, "rb") as audio_file:

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    return transcript.text