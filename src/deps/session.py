from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import session_factory


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
