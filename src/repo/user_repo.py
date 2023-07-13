from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src import schemas
from src.database.models import User
from .base import SQLAlchemyRepo
from .exceptions import RepoError


class UserRepo(SQLAlchemyRepo):

    async def get_users(self) -> list[schemas.User]:
        stmt = select(User)

        result = await self._session.scalars(stmt)

        return [schemas.User.model_validate(user) for user in result]

    async def get_user_with_items(self, user_id: UUID) -> schemas.UserWithItems:
        stmt = select(User).where(User.id == user_id).options(joinedload(User.items))

        result = await self._session.scalar(stmt)

        if result is None:
            raise RepoError("User not found")

        return schemas.UserWithItems.model_validate(result)
