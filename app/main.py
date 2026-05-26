from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.ai.openai_service import ask_jarvis
from app.routes.inspection import router as inspection_router
from app.routes.voice import router as voice_router

app = FastAPI(title="Jarvis Fire Inspector")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Jarvis Fire Inspector Online"}


@app.post("/ask")
def ask(question: Question):
    response = ask_jarvis(question.question)
    return {"response": response}


app.include_router(inspection_router)
app.include_router(voice_router)