from datetime import datetime, timedelta

import jwt
from fastapi.security import HTTPBearer
from passlib.context import CryptContext

from src import schemas
from src.core.config import app_config
from src.database.models import User
from src.exceptions.auth import ExpiredAccessToken, InvalidAccessToken
from src.repo.user_repo import UserRepo


class Authenticator:
    _algorithm = "HS256"
    _access_token_expires_minutes = 60

    auth_scheme = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _secret_key = app_config.jwt_secret_key

    def validated_token_payload(self, access_token: str) -> schemas.TokenPayload:
        try:
            payload = jwt.decode(
                access_token,
                key=self._secret_key,
                algorithms=[self._algorithm]
            )
            return schemas.TokenPayload(**payload)
        except jwt.ExpiredSignatureError:
            raise ExpiredAccessToken
        except jwt.InvalidSignatureError:
            raise InvalidAccessToken

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, user: User) -> str:
        to_encode = {
            "sub": {"user_id": str(user.id)},
            "exp": datetime.utcnow() + timedelta(minutes=self._access_token_expires_minutes),
        }
        encoded_jwt = jwt.encode(to_encode, self._secret_key, algorithm=self._algorithm)
        return encoded_jwt

    async def authenticate_user(self, user_repo: UserRepo, username: str, password: str) -> User | None:
        user = await user_repo.get_by_username(username, raise_exc=False)
        if not user:
            return

        if not self.verify_password(password, user.hashed_password):
            return

        return user
