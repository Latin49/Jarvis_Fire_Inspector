from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.ai.openai_service import ask_jarvis
from app.routes.inspection import router as inspection_router
from app.routes.voice import router as voice_router

from fastapi.responses import Response
from openai import OpenAI
import os

app = FastAPI(title="Jarvis Fire Inspector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


from fastapi.responses import Response
from openai import OpenAI
import os

class Question(BaseModel):
    question: str

class SpeakRequest(BaseModel):
    text: str


@app.post("/speak")
def speak(request: SpeakRequest):
    audio = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="onyx",
        input=request.text,
    )

    return Response(
        content=audio.content,
        media_type="audio/mpeg",
    )


@app.get("/")
def root():
    return {"message": "Jarvis Fire Inspector Online"}


@app.post("/ask")
def ask(question: Question):
    response = ask_jarvis(question.question)
    return {"response": response}


app.include_router(inspection_router)
app.include_router(voice_router)