import logging

from fastapi import FastAPI

from src.api import setup_routers
from src.exceptions.exc_handlers import setup_exc_handlers

logging.basicConfig(format='%(levelname)s [%(asctime)s / %(filename)s]: %(message)s', level=logging.INFO)


def app_builder():
    _app = FastAPI()

    setup_routers(_app)
    setup_exc_handlers(_app)

    return _app


app = app_builder()
