import pytest
from pydantic_core import PydanticCustomError
from app.core.validators import validate_no_spaces

def test_validate_no_spaces_success():
    assert validate_no_spaces("nospaces") == "nospaces"
    assert validate_no_spaces("12345") == "12345"
    assert validate_no_spaces("") == ""

def test_validate_no_spaces_failure():
    with pytest.raises(PydanticCustomError) as excinfo:
        validate_no_spaces("has spaces")
    assert excinfo.value.type == "string_no_spaces_allowed"
    
    with pytest.raises(PydanticCustomError):
        validate_no_spaces(" ")
    
    with pytest.raises(PydanticCustomError):
        validate_no_spaces("leading ")
    
    with pytest.raises(PydanticCustomError):
        validate_no_spaces(" trailing")
