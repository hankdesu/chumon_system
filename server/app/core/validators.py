from typing import Annotated
from pydantic import AfterValidator
from pydantic_core import PydanticCustomError


def validate_no_spaces(v: str) -> str:
    if any(char.isspace() for char in v):
        raise PydanticCustomError("string_no_spaces_allowed", "Cannot contain spaces")
    return v


NoSpaceStr = Annotated[str, AfterValidator(validate_no_spaces)]
