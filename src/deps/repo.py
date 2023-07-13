from typing import Type, AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.repo.base import SQLAlchemyRepo
from .stub import Stub


def get_repo(repo: Type[SQLAlchemyRepo]):

    async def dep(session: AsyncSession = Depends(Stub(AsyncSession))) -> AsyncGenerator[SQLAlchemyRepo, None]:
        yield repo(session)

    return dep
