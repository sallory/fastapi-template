from fastapi import APIRouter, Depends

from src import schemas
from src.repo.user_repo import UserRepo

router = APIRouter()


@router.get("/")
async def read_users(
        user_repo: UserRepo = Depends(),
) -> list[schemas.User]:
    """
    Retrieve users.
    """
    users = await user_repo.get_users()
    return users
