import os
from typing import Optional

from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from app.database import init_db
from app.chat import stream_chat
from app.auth import (
    auth_backend,
    bearer_backend,
    fastapi_users,
    UserRead,
    UserCreate,
    create_db_and_tables,
    current_active_user,
    User
)

app = FastAPI(title="Chat Researcher")

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    # Erlaube SharePoint und Office 365 Domains, die App in einem Iframe anzuzeigen.
    # Kann in der .env über ALLOWED_FRAME_ANCESTORS eingeschränkt werden.
    allowed_ancestors = os.getenv("ALLOWED_FRAME_ANCESTORS", "https://*.sharepoint.com https://*.office.com")
    response.headers["Content-Security-Policy"] = f"frame-ancestors 'self' {allowed_ancestors}"
    
    # X-Frame-Options entfernen, da es sonst zu Konflikten mit frame-ancestors kommen kann
    if "X-Frame-Options" in response.headers:
        del response.headers["X-Frame-Options"]
        
    return response


# Auth Routers
app.include_router(
    fastapi_users.get_auth_router(bearer_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
# registration enabled to create first user
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    init_db()
    await create_db_and_tables()


class ChatRequest(BaseModel):
    messages: list[dict] = []   # prior conversation history
    message: str                # new user message


@app.post("/chat")
async def chat(request: ChatRequest, user: User = Depends(current_active_user)):
    return StreamingResponse(
        stream_chat(request.messages, request.message),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/login")
def login():
    return FileResponse("static/login.html")


@app.get("/")
async def root():
    return FileResponse("static/chat.html")
