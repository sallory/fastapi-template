from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.deps import Stub


class SQLAlchemyRepo:
    def __init__(self, session: AsyncSession = Depends(Stub(AsyncSession))) -> None:
        self._session = session

