from .base import SQLAlchemyRepo
from sqlalchemy import select

from src import schemas
from src.database.models import User


class UserRepo(SQLAlchemyRepo):

    async def get_users(self) -> list[schemas.User]:
        query = select(User)

        result = await self._session.scalars(query)
        users: list = list(result)

        return [schemas.User.model_validate(user) for user in users]
