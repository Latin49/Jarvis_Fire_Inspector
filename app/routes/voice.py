from fastapi import APIRouter, UploadFile, File
from openai import OpenAI
import os

#from app.knowledge.hybrid_answer import answer_with_hybrid_research


router = APIRouter()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


@router.post("/voice-ask")
async def voice_ask(file: UploadFile = File(...)):

    audio_bytes = await file.read()

    temp_file = "uploaded_voice.wav"

    with open(temp_file, "wb") as f:
        f.write(audio_bytes)

    with open(temp_file, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    #answer = answer_with_hybrid_research(transcript.text)

    speech = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="onyx",
        input=answer
    )

    output_file = "jarvis_cloud_response.mp3"
    speech.stream_to_file(output_file)

    return {
        "transcription": transcript.text,
        "answer": answer,
        "audio_file": output_file
    }