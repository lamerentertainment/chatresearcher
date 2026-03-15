from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from app.database import init_db
from app.chat import stream_chat

app = FastAPI(title="Chat Researcher")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup():
    init_db()


class ChatRequest(BaseModel):
    messages: list[dict] = []   # prior conversation history
    message: str                # new user message


@app.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(
        stream_chat(request.messages, request.message),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/")
def root():
    return FileResponse("static/index.html")
