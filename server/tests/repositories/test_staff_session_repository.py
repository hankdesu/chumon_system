import pytest
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime, timezone, timedelta
from app.repositories.staff_session_repository import StaffSessionRepository
from app.models.staff_session import StaffSession

@pytest.fixture
def mock_db_session():
    mock = AsyncMock()
    mock.add = MagicMock()  # add is synchronous
    return mock

@pytest.fixture
def staff_session_repository(mock_db_session):
    return StaffSessionRepository(db_session=mock_db_session)

@pytest.mark.asyncio
async def test_create_staff_session(staff_session_repository, mock_db_session):
    # Arrange
    session_data = StaffSession(session_id="session123", staff_id=1, expires_at=datetime.now(timezone.utc))

    # Act
    result = await staff_session_repository.create_staff_session(session_data)

    # Assert
    assert result == session_data
    mock_db_session.add.assert_called_once_with(session_data)
    mock_db_session.flush.assert_called_once()

@pytest.mark.asyncio
async def test_get_by_session_id(staff_session_repository, mock_db_session):
    # Arrange
    session_id = "session123"
    expected_session = StaffSession(session_id=session_id, staff_id=1, expires_at=datetime.now(timezone.utc))
    
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = expected_session
    mock_db_session.execute.return_value = mock_result

    # Act
    result = await staff_session_repository.get_by_session_id(session_id)

    # Assert
    assert result == expected_session
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_delete_by_staff_id(staff_session_repository, mock_db_session):
    # Arrange
    staff_id = 1
    mock_db_session.execute.return_value = MagicMock()

    # Act
    result = await staff_session_repository.delete_by_staff_id(staff_id)

    # Assert
    assert result is not None
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_delete_expired_by_staff_id(staff_session_repository, mock_db_session):
    # Arrange
    staff_id = 1
    current_time = datetime.now(timezone.utc)
    mock_db_session.execute.return_value = MagicMock()

    # Act
    result = await staff_session_repository.delete_expired_by_staff_id(staff_id, current_time)

    # Assert
    assert result is not None
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_delete_expired_by_staff_id_default_time(staff_session_repository, mock_db_session):
    # Arrange
    staff_id = 1
    mock_db_session.execute.return_value = MagicMock()

    # Act
    result = await staff_session_repository.delete_expired_by_staff_id(staff_id)

    # Assert
    assert result is not None
    mock_db_session.execute.assert_called_once()
