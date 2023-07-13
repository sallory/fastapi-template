from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src import schemas
from src.database.models import Item
from .base import SQLAlchemyRepo


class ItemRepo(SQLAlchemyRepo):

    async def get_items(self) -> list[schemas.Item]:
        query = select(Item)

        result = await self._session.scalars(query)

        return [schemas.Item.model_validate(item) for item in result]

    async def get_items_with_user(self) -> list[schemas.ItemWithUser]:
        query = select(Item).options(joinedload(Item.user))

        result = await self._session.scalars(query)

        return [schemas.ItemWithUser.model_validate(item) for item in result]
