import pytest
from unittest.mock import AsyncMock
from app.core.deps import require_current_staff
from app.core.exceptions import AuthenticationRequiredException

@pytest.mark.asyncio
async def test_require_current_staff_success():
    mock_auth_service = AsyncMock()
    mock_staff = {"id": 1, "username": "test_staff"}
    mock_auth_service.verify_session.return_value = mock_staff
    
    session_id = "valid_session_id"
    result = await require_current_staff(chumon_session_id=session_id, auth_service=mock_auth_service)
    
    assert result == mock_staff
    mock_auth_service.verify_session.assert_called_once_with(session_id)

@pytest.mark.asyncio
async def test_require_current_staff_no_session():
    mock_auth_service = AsyncMock()
    
    with pytest.raises(AuthenticationRequiredException):
        await require_current_staff(chumon_session_id=None, auth_service=mock_auth_service)
    
    mock_auth_service.verify_session.assert_not_called()
