from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials

from src import schemas
from src.repo.user_repo import UserRepo
from src.services.auth import Authenticator

from .repo import get_repo


async def authenticated_user(
        auth_credentials: HTTPAuthorizationCredentials = Depends(Authenticator.auth_scheme),
        authenticator: Authenticator = Depends(),
        user_repo: UserRepo = Depends(get_repo(UserRepo)),
) -> schemas.User:
    token_payload = authenticator.validated_token_payload(auth_credentials.credentials)
    user = await user_repo.get(token_payload.sub.user_id)
    return user
