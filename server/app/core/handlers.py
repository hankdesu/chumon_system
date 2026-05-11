from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.logger import error_logger
from app.core.exceptions import AppException


async def app_exception_handler(request: Request, exception: AppException):
    error_logger.exception(
        f"App exception - Code: {exception.error_code} - Msg: {exception.message}"
    )
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "code": exception.error_code,
            "message": exception.message,
            "data": None,
        },
    )


async def http_exception_handler(request: Request, exception: StarletteHTTPException):
    error_logger.exception(
        f"Http exception - {exception.status_code} - Msg: {exception.detail}"
    )
    return JSONResponse(
        status_code=exception.status_code,
        content={"code": "0001", "message": "Something went wrong!", "data": None},
    )


async def validation_exception_handler(
    request: Request, exception: RequestValidationError
):
    error_logger.exception(f"Request validation error - {exception.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "code": "0002",
            "message": "Request validation error!",
            "data": exception.errors(),
        },
    )


async def global_exception_handler(request: Request, exception: Exception):
    error_logger.exception("Unexpected exception")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"code": "-1", "message": "Internal server error!", "data": None},
    )


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(AppException, app_exception_handler)  # type: ignore
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)  # type: ignore
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore
    app.add_exception_handler(Exception, global_exception_handler)  # type: ignore
