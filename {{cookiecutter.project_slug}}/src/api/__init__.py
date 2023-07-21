from fastapi import APIRouter, FastAPI

from .v1 import v1_router


api_router = APIRouter()

api_router.include_router(v1_router, prefix="/v1")


def setup_routers(app: FastAPI):
    app.include_router(api_router, prefix="/api")
