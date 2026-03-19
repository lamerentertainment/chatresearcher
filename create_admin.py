import asyncio
from app.auth import get_user_db, get_user_manager, UserCreate, async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

async def create_admin(email: str, password: str):
    async with async_session_maker() as session:
        async with asynccontextmanager(get_user_db)(session) as user_db:
            async with asynccontextmanager(get_user_manager)(user_db) as user_manager:
                user = await user_manager.create(
                    UserCreate(email=email, password=password, is_superuser=True, is_active=True)
                )
                print(f"Admin user created: {user.email}")

if __name__ == "__main__":
    import sys
    # Add project root to sys.path
    import os
    sys.path.append(os.getcwd())
    
    email = input("Admin Email: ")
    password = input("Admin Password: ")
    asyncio.run(create_admin(email, password))
