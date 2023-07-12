from fastapi import APIRouter

from .endpoints import users


v1_router = APIRouter()

v1_router.include_router(users.router, prefix="/users")

