from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from .users import User


class ItemBase(BaseModel):
    name: Optional[str] = None


class ItemWithUserBase(ItemBase):
    user: Optional[User] = None


class ItemCreate(ItemWithUserBase):
    pass


class ItemUpdate(ItemWithUserBase):
    pass


class Item(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[UUID] = None


class ItemWithUser(Item, ItemWithUserBase):
    pass


class UserWithItems(User):
    items: list[Item]
