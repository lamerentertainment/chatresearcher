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
    return user

async def current_active_user_simplified(
    request: Request,
    session: AsyncSession = Depends(get_async_session)
) -> User:
    # 1. Check if the request comes from SharePoint
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
        return await get_sharepoint_user(session)

    # 2. Check for admin session cookie
    auth_token = request.cookies.get("admin_auth")
    # Debug logging
    print(f"DEBUG: Cookie 'admin_auth' found: {auth_token is not None}")
    if auth_token:
        print(f"DEBUG: Cookie value length: {len(auth_token)}")
    
    if auth_token and auth_token.strip() == ADMIN_PASSWORD:
        return await get_admin_user(session)

    # 3. Fallback: If not authenticated, raise error or redirect (handled in main.py)
    print(f"DEBUG: Auth failed for {request.url.path}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
    )
