import logging

from fastapi import FastAPI

from src.api import api_router

logging.basicConfig(format='%(levelname)s [%(asctime)s / %(filename)s]: %(message)s', level=logging.INFO)

app = FastAPI()

app.include_router(api_router, prefix="/api")


def app_builder():
    pass