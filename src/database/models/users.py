from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=sa.func.gen_random_uuid())
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(server_default=sa.True_())
