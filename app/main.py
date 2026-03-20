import os
import json
from typing import Optional

from fastapi import FastAPI, Depends, Request, HTTPException, BackgroundTasks, Form, status
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
    current_active_user_simplified,
    UserRequest,
    get_async_session,
    SECURE_COOKIES,
    ADMIN_PASSWORD,
    User
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title="Chat Researcher")

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    # Erlaube SharePoint und Office 365 Domains, die App in einem Iframe anzuzeigen.
    # Kann in der .env über ALLOWED_FRAME_ANCESTORS eingeschränkt werden.
    allowed_ancestors = os.getenv("ALLOWED_FRAME_ANCESTORS", "https://*.sharepoint.com https://*.office.com").replace(',', ' ')
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
# Cookie-based auth for browser access
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
# registration enabled to create first user
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.get("/debug/me")
async def debug_me(request: Request):
    user = None
    try:
        user = await current_active_user(request)
    except:
        pass
    
    return {
        "user": {
            "email": user.email,
            "is_superuser": user.is_superuser,
            "is_active": user.is_active
        } if user else None,
        "headers": dict(request.headers),
        "cookies": request.cookies
    }

# Admin Routes
@app.get("/admin/users", tags=["admin"])
async def list_users(
    user: User = Depends(current_active_user_simplified),
    session: AsyncSession = Depends(get_async_session)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    result = await session.execute(select(User))
    return result.scalars().all()

@app.get("/admin/requests", tags=["admin"])
async def list_requests(
    user: User = Depends(current_active_user_simplified),
    session: AsyncSession = Depends(get_async_session)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    result = await session.execute(select(UserRequest).order_by(UserRequest.timestamp.desc()).limit(100))
    return result.scalars().all()

async def log_user_request(user_id: int, query: str, metrics_gen):
    pass # Replaced by save_request_to_db and wrapped_stream

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    init_db()
    await create_db_and_tables()


class ChatRequest(BaseModel):
    messages: list[dict] = []   # prior conversation history
    message: str                # new user message


@app.post("/chat")
async def chat(
    request: ChatRequest, 
    background_tasks: BackgroundTasks,
    user: User = Depends(current_active_user_simplified)
):
    async def wrapped_stream():
        tokens_input = 0
        tokens_output = 0
        cost_usd = 0.0
        
        async for chunk in stream_chat(request.messages, request.message):
            yield chunk
            
            # Extract metrics from the 'done' event
            if chunk.startswith("data: "):
                try:
                    data = json.loads(chunk[6:])
                    if data.get("type") == "done":
                        tokens_input = data.get("tokens_input", 0)
                        tokens_output = data.get("tokens_output", 0)
                        cost_usd = data.get("cost_usd", 0.0)
                except:
                    pass
        
        # Log to database after the stream is finished
        background_tasks.add_task(
            save_request_to_db,
            user_id=user.id,
            query=request.message,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            cost_usd=cost_usd
        )

    return StreamingResponse(
        wrapped_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )

async def save_request_to_db(user_id: int, query: str, tokens_input: int, tokens_output: int, cost_usd: float):
    from app.auth import async_session_maker
    async with async_session_maker() as session:
        new_request = UserRequest(
            user_id=user_id,
            query=query,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            cost_usd=cost_usd
        )
        session.add(new_request)
        await session.commit()


@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login")
    response.delete_cookie("__session")
    response.delete_cookie("chatresearcher_auth")
    return response

@app.get("/login")
def login():
    return FileResponse("static/login.html")

@app.post("/login")
async def login_post(password: str = Form(...)):
    if password.strip() == ADMIN_PASSWORD:
        print(f"DEBUG: Login successful. Setting cookie '__session'.")
        response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(
            key="__session", 
            value=ADMIN_PASSWORD, 
            path="/",
            httponly=True, 
            samesite="lax",
            secure=SECURE_COOKIES
        )
        return response
    print(f"DEBUG: Login failed. Provided password: {password[:1]}***")
    return RedirectResponse(url="/login?error=1", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/")
async def root(request: Request, session: AsyncSession = Depends(get_async_session)):
    try:
        user = await current_active_user_simplified(request, session)
        response = FileResponse("static/chat.html")
        
        # If authorized via referer (SharePoint), ensure we set the session cookie
        # so subsequent fetch calls (which might lose the referer) work.
        referer = request.headers.get("referer", "")
        origin = request.headers.get("origin", "")
        
        from app.auth import ALLOWED_DOMAINS
        is_sharepoint = False
        for domain in ALLOWED_DOMAINS.split():
            clean_domain = domain.replace("https://", "").replace("http://", "").replace("*.", "")
            if clean_domain and (clean_domain in referer or clean_domain in origin):
                is_sharepoint = True
                break
        
        if is_sharepoint:
            # Only set if not already authenticated as admin
            if not (user and user.is_superuser):
                response.set_cookie(
                    key="__session",
                    value="sharepoint-access",
                    path="/",
                    httponly=True,
                    samesite="lax",
                    secure=SECURE_COOKIES
                )
        return response
    except HTTPException:
        return RedirectResponse(url="/login")
