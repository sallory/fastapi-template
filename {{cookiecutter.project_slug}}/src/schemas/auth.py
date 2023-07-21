from uuid import UUID

from pydantic import BaseModel


class TokenSub(BaseModel):
    user_id: UUID


class TokenPayload(BaseModel):
    sub: TokenSub
    exp: int


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
