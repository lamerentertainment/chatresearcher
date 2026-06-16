import os
import json
from google.cloud import firestore
from typing import Optional

from fastapi import FastAPI, Depends, Request, HTTPException, BackgroundTasks, Form, status
from fastapi.responses import StreamingResponse, FileResponse, RedirectResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Prioritize loading tenant-specific environment files if TENANT is specified
tenant = os.getenv("TENANT")
if tenant and os.path.exists(f".env.{tenant}"):
    load_dotenv(f".env.{tenant}")
load_dotenv()

# URL of the Cloud Run service itself (set as env var in Cloud Run).
# Used so the browser can call /chat directly, bypassing Firebase CDN buffering.
CLOUD_RUN_URL = os.getenv("CLOUD_RUN_URL", "")

from app.database import init_db
from app.chat import stream_chat, SYSTEM_PROMPT, DEFAULT_WELCOME_MESSAGE
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
    User,
    generate_token_for_user,
    get_admin_user,
    get_user_manager
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title="Chat Researcher")
firestore_db = firestore.AsyncClient()

# CORS: allow the Firebase Hosting domain to call Cloud Run directly (for SSE streaming).
# Set CORS_ORIGINS as comma-separated list in Cloud Run env vars,
# e.g. "https://gen-lang-client-0915148106.web.app,https://gen-lang-client-0915148106.firebaseapp.com"
_cors_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]
if _cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"],
    )

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
    request: Request,
    as_json: bool = False,
    user: User = Depends(current_active_user_simplified),
    session: AsyncSession = Depends(get_async_session)
):
    print(f"DEBUG: list_requests accessed by user: {getattr(user, 'email', 'unknown')}, is_superuser: {getattr(user, 'is_superuser', False)}")
    if not user.is_superuser:
        if as_json:
            raise HTTPException(status_code=403, detail="Forbidden")
        return RedirectResponse(url="/login?redirect=/admin/requests")
    
    if as_json:
        tenant = os.getenv("TENANT", "krg")
        requests_ref = firestore_db.collection("requests")
        
        try:
            # Try optimized query (requires composite index)
            query = requests_ref.where("tenant", "==", tenant).order_by("timestamp", direction=firestore.Query.DESCENDING).limit(100)
            docs = await query.get()
        except Exception as e:
            # Fallback for missing composite index or other Firestore query issues
            print(f"WARNING: Firestore sorted query failed: {e}")
            print("Attempting fallback: fetching documents and sorting in memory.")
            
            try:
                fallback_query = requests_ref.where("tenant", "==", tenant)
                all_docs = await fallback_query.get()
                
                from datetime import datetime, timezone
                def get_timestamp(doc):
                    data = doc.to_dict()
                    ts = data.get("timestamp")
                    if ts:
                        if isinstance(ts, datetime):
                            if ts.tzinfo is None:
                                return ts.replace(tzinfo=timezone.utc)
                            return ts
                        try:
                            return datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
                        except Exception:
                            pass
                    return datetime.min.replace(tzinfo=timezone.utc)
                
                docs = sorted(all_docs, key=get_timestamp, reverse=True)[:100]
            except Exception as fallback_err:
                print(f"ERROR: Fallback query also failed: {fallback_err}")
                docs = []
        
        requests = []
        for doc in docs:
            data = doc.to_dict()
            # Convert timestamp to ISO string for JSON
            ts = data.get("timestamp")
            if ts:
                if hasattr(ts, "isoformat"):
                    ts_str = ts.isoformat()
                else:
                    ts_str = str(ts)
            else:
                ts_str = None
                
            requests.append({
                "id": doc.id,
                "timestamp": ts_str,
                "query": data.get("query"),
                "response": data.get("response", ""),
                "tokens_input": data.get("tokens_input", 0),
                "tokens_output": data.get("tokens_output", 0),
                "cost_usd": data.get("cost_usd", 0.0),
                "user_email": data.get("user_email", "unknown")
            })
        return requests
    
    return FileResponse("static/admin_requests.html")


@app.get("/admin/settings", tags=["admin"])
async def admin_settings_page(
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        return RedirectResponse(url="/login?redirect=/admin/settings")
    return FileResponse("static/admin_settings.html")


@app.get("/api/config")
async def get_public_config():
    tenant = os.getenv("TENANT", "krg")
    try:
        doc = await firestore_db.collection("settings").document(tenant).get()
        if doc.exists:
            data = doc.to_dict()
            return {"welcome_message": data.get("welcome_message") or DEFAULT_WELCOME_MESSAGE}
    except Exception as e:
        print(f"Error fetching welcome message from Firestore: {e}")
    return {"welcome_message": DEFAULT_WELCOME_MESSAGE}


@app.get("/api/admin/config", tags=["admin"])
async def get_admin_config(
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    tenant = os.getenv("TENANT", "krg")
    try:
        doc = await firestore_db.collection("settings").document(tenant).get()
        if doc.exists:
            data = doc.to_dict()
            return {
                "system_prompt": data.get("system_prompt") or SYSTEM_PROMPT,
                "welcome_message": data.get("welcome_message") or DEFAULT_WELCOME_MESSAGE
            }
    except Exception as e:
        print(f"Error fetching config: {e}")
    return {"system_prompt": SYSTEM_PROMPT, "welcome_message": DEFAULT_WELCOME_MESSAGE}


class ConfigUpdateRequest(BaseModel):
    system_prompt: str
    welcome_message: str


@app.post("/api/admin/config", tags=["admin"])
async def save_admin_config(
    data: ConfigUpdateRequest,
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    tenant = os.getenv("TENANT", "krg")
    try:
        await firestore_db.collection("settings").document(tenant).set({
            "system_prompt": data.system_prompt,
            "welcome_message": data.welcome_message
        }, merge=True)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SkillSaveRequest(BaseModel):
    id: str
    name: str
    content: str
    is_active: bool


@app.get("/api/admin/skills", tags=["admin"])
async def list_admin_skills(
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    tenant = os.getenv("TENANT", "krg")
    try:
        docs = await firestore_db.collection("skills").where("tenant", "==", tenant).get()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/admin/skills", tags=["admin"])
async def save_admin_skill(
    skill: SkillSaveRequest,
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    tenant = os.getenv("TENANT", "krg")
    try:
        doc_id = f"{tenant}_{skill.id}"
        await firestore_db.collection("skills").document(doc_id).set({
            "id": skill.id,
            "tenant": tenant,
            "name": skill.name,
            "content": skill.content,
            "is_active": skill.is_active
        })
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/admin/skills/{skill_id}", tags=["admin"])
async def delete_admin_skill(
    skill_id: str,
    user: User = Depends(current_active_user_simplified)
):
    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden")
    tenant = os.getenv("TENANT", "krg")
    try:
        doc_id = f"{tenant}_{skill_id}"
        await firestore_db.collection("skills").document(doc_id).delete()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
    model: str = "claude-sonnet-4-6"


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
        response_text = ""
        
        async for chunk in stream_chat(request.messages, request.message, model=request.model):
            yield chunk
            
            # Extract metrics from the 'done' event and accumulate chatbot response
            if chunk.startswith("data: "):
                try:
                    data = json.loads(chunk[6:])
                    if data.get("type") == "done":
                        tokens_input = data.get("tokens_input", 0)
                        tokens_output = data.get("tokens_output", 0)
                        cost_usd = data.get("cost_usd", 0.0)
                    elif data.get("type") == "text":
                        response_text += data.get("content", "")
                except:
                    pass
        
        # Log to Firestore after the stream is finished
        background_tasks.add_task(
            save_request_to_firestore,
            user_id=user.id,
            user_email=user.email,
            query=request.message,
            response=response_text,
            tokens_input=tokens_input,
            tokens_output=tokens_output,
            cost_usd=cost_usd
        )

    return StreamingResponse(
        wrapped_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache, no-transform, must-revalidate",
            "X-Accel-Buffering": "no",
            "X-Content-Type-Options": "nosniff",
            "Connection": "keep-alive",
            "Content-Encoding": "identity",
        },
    )

async def save_request_to_firestore(user_id: int, user_email: str, query: str, response: str, tokens_input: int, tokens_output: int, cost_usd: float):
    try:
        tenant = os.getenv("TENANT", "krg")
        await firestore_db.collection("requests").add({
            "tenant": tenant,
            "user_id": user_id,
            "user_email": user_email,
            "query": query,
            "response": response,
            "tokens_input": tokens_input,
            "tokens_output": tokens_output,
            "cost_usd": cost_usd,
            "timestamp": firestore.SERVER_TIMESTAMP
        })
    except Exception as e:
        print(f"Error saving to Firestore: {e}")

async def save_request_to_db(user_id: int, query: str, tokens_input: int, tokens_output: int, cost_usd: float):
    # Keep the old SQLite logging as a backup for now if desired, or remove it.
    # For now, let's keep the function name but point to Firestore in chat() above.
    pass


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
async def login_post(password: str = Form(...), session: AsyncSession = Depends(get_async_session)):
    if password.strip() == ADMIN_PASSWORD:
        admin_user = await get_admin_user(session)
        token = await generate_token_for_user(admin_user)
        response = JSONResponse({"token": token})
        response.set_cookie(
            key="__session", 
            value=ADMIN_PASSWORD, 
            path="/",
            httponly=True, 
            samesite="lax",
            secure=SECURE_COOKIES
        )
        return response
    
    print(f"DEBUG: Login failed.")
    raise HTTPException(status_code=401, detail="Falsches Passwort")


@app.get("/")
async def root(
    request: Request, 
    session: AsyncSession = Depends(get_async_session),
    user_manager = Depends(get_user_manager)
):
    try:
        user = await current_active_user_simplified(request, session, user_manager)
        token_for_client = await generate_token_for_user(user)
        
        # Check if Hermes is enabled
        hermes_key = os.getenv("HERMES_API_KEY")
        hermes_url = os.getenv("HERMES_URL")
        hermes_local_enabled = "true" if hermes_key and hermes_url else "false"

        hermes_remote_key = os.getenv("HERMES_REMOTE_API_KEY")
        hermes_remote_url = os.getenv("HERMES_REMOTE_URL")
        hermes_remote_enabled = "true" if hermes_remote_key and hermes_remote_url else "false"

        hermes_enabled = "true" if (hermes_key and hermes_url) or (hermes_remote_key and hermes_remote_url) else "false"
        
        # Generate HTML with injected token
        with open("static/chat.html", "r") as f:
            html_content = f.read()
            
        html_content = html_content.replace(
            "// Authentication Check",
            f"// Authentication Check\n  window.BACKEND_URL = window.location.hostname.endsWith('.run.app') ? window.location.origin : '{CLOUD_RUN_URL}';\n  window.HERMES_ENABLED = {hermes_enabled};\n  window.HERMES_LOCAL_ENABLED = {hermes_local_enabled};\n  window.HERMES_REMOTE_ENABLED = {hermes_remote_enabled};\n  const INJECTED_TOKEN = '{token_for_client}';\n  if (INJECTED_TOKEN) localStorage.setItem('chatresearcher_token', INJECTED_TOKEN);"
        )
        
        response = HTMLResponse(content=html_content)
        
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
