from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from src import schemas, deps
from src.exceptions import repo as repo_exc
from src.repo.user_repo import UserRepo
from src.services.auth import Authenticator

router = APIRouter()


@router.post("/")
async def create_user(
        user_in: schemas.UserCreate,
        authenticator: Authenticator = Depends(),
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> schemas.User:
    """
    Create User.
    """
    hashed_password = authenticator.get_password_hash(user_in.password)
    user = await user_repo.create(user_in, hashed_password)
    return user


@router.get("/")
async def read_users(
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> list[schemas.User]:
    """
    Retrieve users.
    """
    users = await user_repo.get_users()
    return users


@router.get("/me")
async def read_user(
        user: schemas.User = Depends(deps.authenticated_user)
) -> schemas.User:
    """
    Retrieve user from the bearer token
    """
    return user


@router.get("/{user_id}")
async def read_users_with_items(
        user_id: UUID,
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> schemas.UserWithItems:
    """
    Retrieve user with items.
    """
    try:
        user = await user_repo.get_user_with_items(user_id)
    except repo_exc.NotFound:
        raise HTTPException(status_code=404, detail="User not found")

    return user
