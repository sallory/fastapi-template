from fastapi import APIRouter

from .endpoints import users, items


v1_router = APIRouter()

v1_router.include_router(users.router, prefix="/users")
v1_router.include_router(items.router, prefix="/items")

