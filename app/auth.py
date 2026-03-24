import os
from datetime import datetime
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin, schemas
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
    BearerTransport,
)
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import ForeignKey, DateTime, Text, Float, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("JWT_SECRET", "SUPER_SECRET_TOKEN_THAT_IS_LONGER_THAN_32_CHARACTERS_FOR_SECURITY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123").strip()
ALLOWED_DOMAINS = os.getenv("ALLOWED_FRAME_ANCESTORS", "https://*.sharepoint.com https://*.office.com").replace(',', ' ')
SECURE_COOKIES = os.getenv("SECURE_COOKIES", "true").lower() == "true"

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    requests: Mapped[list["UserRequest"]] = relationship("UserRequest", back_populates="user")

class UserRequest(Base):
    __tablename__ = "user_request"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    query: Mapped[str] = mapped_column(Text)
    response: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    tokens_input: Mapped[int] = mapped_column(Integer, default=0)
    tokens_output: Mapped[int] = mapped_column(Integer, default=0)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)

    user: Mapped["User"] = relationship("User", back_populates="requests")

engine = create_async_engine("sqlite+aiosqlite:///./data/users.db")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session():
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

cookie_transport = CookieTransport(
    cookie_name="chatresearcher_auth",
    cookie_max_age=3600,
    cookie_samesite="lax",
    cookie_secure=SECURE_COOKIES
)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="auth",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

bearer_backend = AuthenticationBackend(
    name="jwt-bearer",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend, bearer_backend],
)

current_active_user = fastapi_users.current_user(active=True)

async def generate_token_for_user(user: User) -> str:
    strategy = JWTStrategy(secret=SECRET, lifetime_seconds=3600, token_audience="fastapi-users:jwt-bearer")
    # The audience must match the bearer backend name for chat to work
    return await strategy.write_token(user)

# Schema definitions
class UserRead(schemas.BaseUser[int]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass

# Simplified Auth Dependency
from fastapi import HTTPException, status
from sqlalchemy import select

async def get_sharepoint_user(session: AsyncSession):
    """Gets or creates a special user for SharePoint access."""
    email = "sharepoint@internal.local"
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        user = User(email=email, hashed_password="!", is_active=True, is_verified=True)
        session.add(user)
        await session.commit()
    return user

async def get_admin_user(session: AsyncSession):
    """Gets or creates the default admin user."""
    email = "admin@internal.local"
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        user = User(email=email, hashed_password="!", is_active=True, is_verified=True, is_superuser=True)
        session.add(user)
        await session.commit()
    elif not user.is_superuser:
        user.is_superuser = True
        session.add(user)
        await session.commit()
    return user

async def current_active_user_simplified(
    request: Request,
    session: AsyncSession = Depends(get_async_session),
    user_manager: UserManager = Depends(get_user_manager)
) -> User:
    print(f"DEBUG: Authentication check for {request.url.path}")
    # 1. Check for token (Priority: Query Param > Authorization Header)
    # Query param is used for the initial page load in iframes after login.
    token = request.query_params.get("token")
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.replace("Bearer ", "")
    
    if token:
        print(f"DEBUG: Token found in {'query_params' if request.query_params.get('token') else 'headers'}. Length: {len(token)}")
        strategy = JWTStrategy(secret=SECRET, lifetime_seconds=3600, token_audience="fastapi-users:jwt-bearer")
        try:
            user = await strategy.read_token(token, user_manager)
            if user:
                if user.is_active:
                    print(f"DEBUG: Authenticated via token. User: {user.email}, Superuser: {user.is_superuser}")
                    return user
                else:
                    print(f"DEBUG: Token auth failed: User {user.email} is not active.")
            else:
                print(f"DEBUG: Token auth failed: strategy.read_token returned None.")
        except Exception as e:
            print(f"DEBUG: Token auth failed with error: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()

    # 2. Check for admin session cookie
    auth_token = request.cookies.get("__session")
    # Debug logging
    print(f"DEBUG: Cookie '__session' found: {auth_token is not None}")
    if auth_token:
        print(f"DEBUG: Cookie value length: {len(auth_token)}")
    
    if auth_token and auth_token.strip() == ADMIN_PASSWORD:
        admin_user = await get_admin_user(session)
        print(f"DEBUG: Authenticated via admin cookie. User: {admin_user.email}, Superuser: {admin_user.is_superuser}")
        return admin_user

    if auth_token and auth_token.strip() == "sharepoint-access":
        sp_user = await get_sharepoint_user(session)
        print(f"DEBUG: Authenticated via sharepoint-access cookie. User: {sp_user.email}, Superuser: {sp_user.is_superuser}")
        return sp_user

    # 3. Check if the request comes from SharePoint (Referer based)
    # BUT: Only for non-admin routes. Admin routes must use explicit auth.
    if not request.url.path.startswith("/admin"):
        referer = request.headers.get("referer", "")
        origin = request.headers.get("origin", "")
        
        # Simple check: if allowed domain is in referer or origin
        is_from_allowed_domain = False
        for domain in ALLOWED_DOMAINS.split():
            clean_domain = domain.replace("https://", "").replace("http://", "").replace("*.", "")
            if clean_domain and (clean_domain in referer or clean_domain in origin):
                is_from_allowed_domain = True
                break
                
        if is_from_allowed_domain:
            sp_user = await get_sharepoint_user(session)
            print(f"DEBUG: Authenticated via domain match ({referer or origin}). User: {sp_user.email}, Superuser: {sp_user.is_superuser}")
            return sp_user

    # 3. Fallback: If not authenticated, raise error or redirect (handled in main.py)
    print(f"DEBUG: Auth failed for {request.url.path}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
    )
