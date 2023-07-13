from uuid import UUID

from fastapi import APIRouter, Depends

from src import schemas, deps
from src.repo.user_repo import UserRepo

router = APIRouter()


@router.get("/")
async def read_users(
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> list[schemas.User]:
    """
    Retrieve users.
    """
    users = await user_repo.get_users()
    return users


@router.get("/{user_id}")
async def read_users_with_items(
        user_id: UUID,
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> schemas.UserWithItems:
    """
    Retrieve users with items.
    """
    user = await user_repo.get_user_with_items(user_id)
    return user
