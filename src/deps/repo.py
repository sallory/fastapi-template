from typing import Type, AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repo.base import SQLAlchemyRepo
from .session import get_async_session


def get_repo(repo: Type[SQLAlchemyRepo]):
    async def dep(session: AsyncSession = Depends(get_async_session)) -> AsyncGenerator[SQLAlchemyRepo, None]:
        yield repo(session)

    return dep
