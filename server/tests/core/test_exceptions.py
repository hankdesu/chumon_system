import pytest
from app.core.exceptions import (
    AppException,
    InvalidCredentialsException,
    InvalidSessionException,
    InvalidStaffException,
    AuthenticationRequiredException,
    DatabaseRecordNotFoundException,
)

def test_app_exception():
    exc = AppException(error_code="9999", message="Test error", status_code=418)
    assert exc.error_code == "9999"
    assert exc.message == "Test error"
    assert exc.status_code == 418

def test_invalid_credentials_exception():
    exc = InvalidCredentialsException()
    assert exc.error_code == "1001"
    assert exc.status_code == 401
    assert exc.message == "Wrong username or password!"

def test_invalid_session_exception():
    exc = InvalidSessionException()
    assert exc.error_code == "1002"
    assert exc.status_code == 401
    assert exc.message == "Invalid or expired session!"

def test_invalid_staff_exception():
    exc = InvalidStaffException()
    assert exc.error_code == "1003"
    assert exc.status_code == 401
    assert exc.message == "Invalid staff!"

def test_authentication_required_exception():
    exc = AuthenticationRequiredException()
    assert exc.error_code == "1004"
    assert exc.status_code == 401
    assert exc.message == "Authentication required!"

def test_database_record_not_found_exception():
    exc = DatabaseRecordNotFoundException()
    assert exc.error_code == "1005"
    assert exc.status_code == 404
    assert exc.message == "Database record not found!"
