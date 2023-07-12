import logging

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from src.api import api_router
from src.deps import get_session, Stub

logging.basicConfig(format='%(levelname)s [%(asctime)s / %(filename)s]: %(message)s', level=logging.INFO)

app = FastAPI()

app.include_router(api_router, prefix="/api")

app.dependency_overrides[Stub(AsyncSession)] = get_session  # noqa
