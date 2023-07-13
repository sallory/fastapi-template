from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import TimedBaseModel


class Item(TimedBaseModel):
    __tablename__ = "items"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=sa.func.gen_random_uuid())
    name: Mapped[str]

    user_id: Mapped[UUID] = mapped_column(sa.ForeignKey("users.id"))
    user = relationship("User", back_populates="items")
