from uuid import UUID

from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload

from src import schemas
from src.database.models import User
from .base import SQLAlchemyRepo
from .exceptions import NotFound


class UserRepo(SQLAlchemyRepo):

    async def create(self, user_in: schemas.UserCreate, hashed_password: str) -> schemas.User:
        stmt = insert(User).returning(User).values(
            username=user_in.username,
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            middle_name=user_in.middle_name,
            hashed_password=hashed_password,
        )

        user = await self._session.scalar(stmt)

        return schemas.User.model_validate(user)

    async def get(self, user_id: UUID) -> schemas.User:
        stmt = select(User).where(User.id == user_id)

        result = await self._session.scalar(stmt)

        if result is None:
            raise NotFound("User not found")

        return schemas.User.model_validate(result)

    async def get_by_username(self, username: str, raise_exc: bool = True) -> User:
        stmt = select(User).where(User.username == username)

        result = await self._session.scalar(stmt)

        if result is None and raise_exc:
            raise NotFound("User not found")

        return result

    async def get_users(self) -> list[schemas.User]:
        stmt = select(User)

        result = await self._session.scalars(stmt)

        return [schemas.User.model_validate(user) for user in result]

    async def get_user_with_items(self, user_id: UUID) -> schemas.UserWithItems:
        stmt = select(User).where(User.id == user_id).options(joinedload(User.items))

        result = await self._session.scalar(stmt)

        if result is None:
            raise NotFound("User not found")

        return schemas.UserWithItems.model_validate(result)
