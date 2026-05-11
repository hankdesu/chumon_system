from pydantic import BaseModel
from typing import TypeVar, Generic, Any

T = TypeVar("T")


class ResponseDto(BaseModel, Generic[T]):
    message: str = "Success"
    data: T | None = None
    meta: dict[str, Any] | None = None
