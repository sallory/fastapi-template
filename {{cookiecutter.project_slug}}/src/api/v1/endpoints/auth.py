from fastapi import APIRouter, Depends, HTTPException, status

from src import schemas, deps
from src.repo.user_repo import UserRepo
from src.services.auth import Authenticator

router = APIRouter()


@router.post("/access-token")
async def get_access_token(
        user_in: schemas.Login,
        authenticator: Authenticator = Depends(),
        user_repo: UserRepo = Depends(deps.get_repo(UserRepo)),
) -> schemas.Token:
    """
    Retrieve access-token
    """
    user = await authenticator.authenticate_user(
        user_repo=user_repo,
        username=user_in.username,
        password=user_in.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = authenticator.create_access_token(user)

    return schemas.Token(access_token=access_token)
