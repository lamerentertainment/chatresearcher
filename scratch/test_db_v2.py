
import asyncio
from sqlalchemy import select
from app.auth import async_session_maker, UserRequest, User

async def test_query():
    async with async_session_maker() as session:
        stmt = (
            select(
                UserRequest.id,
                UserRequest.timestamp,
                UserRequest.query,
                UserRequest.tokens_input,
                UserRequest.tokens_output,
                UserRequest.cost_usd,
                User.email
            )
            .join(User, UserRequest.user_id == User.id)
            .order_by(UserRequest.timestamp.desc())
            .limit(100)
        )
        result = await session.execute(stmt)
        requests = []
        for row in result.all():
            requests.append({
                "id": row.id,
                "timestamp": row.timestamp.isoformat() if row.timestamp else None,
                "query": row.query,
                "tokens_input": row.tokens_input,
                "tokens_output": row.tokens_output,
                "cost_usd": row.cost_usd,
                "user_email": row.email
            })
        
        print(f"Found {len(requests)} requests")
        for req in requests[:5]:
            print(f"ID: {req.id}, User: {req.user_email}, Query: {req.query}")

if __name__ == "__main__":
    asyncio.run(test_query())
