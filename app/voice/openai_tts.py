from openai import OpenAI
from playsound import playsound

import os
import time


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def speak_natural(text: str):

    filename = f"jarvis_response_{int(time.time())}.mp3"

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="onyx",
        input=text
    )

    response.stream_to_file(filename)

    playsound(filename)