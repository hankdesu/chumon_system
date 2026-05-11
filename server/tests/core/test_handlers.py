import pytest
from unittest.mock import MagicMock, patch, call
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.exceptions import AppException
from app.core.handlers import (
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler,
    register_exception_handlers,
)

@pytest.mark.asyncio
async def test_app_exception_handler():
    request = MagicMock(spec=Request)
    exception = AppException(error_code="1234", message="App error", status_code=400)
    
    with patch("app.core.handlers.error_logger") as mock_logger:
        response = await app_exception_handler(request, exception)
        
        assert response.status_code == 400
        assert response.body == b'{"code":"1234","message":"App error","data":null}'
        mock_logger.exception.assert_called_once()

@pytest.mark.asyncio
async def test_http_exception_handler():
    request = MagicMock(spec=Request)
    exception = StarletteHTTPException(status_code=404, detail="Not Found")
    
    with patch("app.core.handlers.error_logger") as mock_logger:
        response = await http_exception_handler(request, exception)
        
        assert response.status_code == 404
        assert response.body == b'{"code":"0001","message":"Something went wrong!","data":null}'
        mock_logger.exception.assert_called_once()

@pytest.mark.asyncio
async def test_validation_exception_handler():
    request = MagicMock(spec=Request)
    exception = RequestValidationError(errors=[{"loc": ["body"], "msg": "field required", "type": "value_error.missing"}])
    
    with patch("app.core.handlers.error_logger") as mock_logger:
        response = await validation_exception_handler(request, exception)
        
        assert response.status_code == 422
        # The response body contains the errors
        import json
        body = json.loads(response.body)
        assert body["code"] == "0002"
        assert body["data"] == exception.errors()
        mock_logger.exception.assert_called_once()

@pytest.mark.asyncio
async def test_global_exception_handler():
    request = MagicMock(spec=Request)
    exception = Exception("Unexpected error")
    
    with patch("app.core.handlers.error_logger") as mock_logger:
        response = await global_exception_handler(request, exception)
        
        assert response.status_code == 500
        assert response.body == b'{"code":"-1","message":"Internal server error!","data":null}'
        mock_logger.exception.assert_called_once_with("Unexpected exception")

def test_register_exception_handlers():
    app = MagicMock()
    register_exception_handlers(app)
    
    # Check if add_exception_handler was called for each exception type
    assert app.add_exception_handler.call_count == 4
    
    # Verify specific calls
    calls = [
        call(AppException, app_exception_handler),
        call(StarletteHTTPException, http_exception_handler),
        call(RequestValidationError, validation_exception_handler),
        call(Exception, global_exception_handler),
    ]
    app.add_exception_handler.assert_has_calls(calls, any_order=True)
