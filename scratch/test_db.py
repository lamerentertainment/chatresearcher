
import asyncio
from sqlalchemy import select
from app.auth import async_session_maker, UserRequest

async def test_query():
    async with async_session_maker() as session:
        result = await session.execute(select(UserRequest).order_by(UserRequest.timestamp.desc()).limit(100))
        requests = result.scalars().all()
        print(f"Found {len(requests)} requests")
        for req in requests[:5]:
            print(f"ID: {req.id}, Query: {req.query}")

if __name__ == "__main__":
    asyncio.run(test_query())
