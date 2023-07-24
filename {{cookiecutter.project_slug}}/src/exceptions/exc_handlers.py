from typing import TypeVar

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_403_FORBIDDEN

from .auth import ExpiredAccessToken, InvalidAccessToken

ExcType = TypeVar("ExcType")


def auth_exception_handler(exc_type: ExcType):
    async def handler(request: Request, exc: ExcType = exc_type):
        return JSONResponse(
            status_code=HTTP_403_FORBIDDEN,
            content={
                "detail": "Not authenticated"
            }
        )

    return handler


def setup_exc_handlers(app: FastAPI):
    app.add_exception_handler(
        ExpiredAccessToken,
        auth_exception_handler(ExpiredAccessToken)
    )
    app.add_exception_handler(
        InvalidAccessToken,
        auth_exception_handler(InvalidAccessToken)
    )
