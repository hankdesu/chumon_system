import pytest
from unittest.mock import AsyncMock, MagicMock
from app.repositories.staff_repository import StaffRepository
from app.models.staff import Staff

@pytest.fixture
def mock_db_session():
    mock = AsyncMock()
    mock.add = MagicMock()  # add is synchronous
    return mock

@pytest.fixture
def staff_repository(mock_db_session):
    return StaffRepository(db_session=mock_db_session)

@pytest.mark.asyncio
async def test_get_by_username(staff_repository, mock_db_session):
    # Arrange
    username = "testuser"
    expected_staff = Staff(id=1, username=username)
    
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = expected_staff
    mock_db_session.execute.return_value = mock_result

    # Act
    result = await staff_repository.get_by_username(username)

    # Assert
    assert result == expected_staff
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_get_by_id(staff_repository, mock_db_session):
    # Arrange
    staff_id = 1
    expected_staff = Staff(id=staff_id, username="testuser")
    mock_db_session.get.return_value = expected_staff

    # Act
    result = await staff_repository.get_by_id(staff_id)

    # Assert
    assert result == expected_staff
    mock_db_session.get.assert_called_once_with(Staff, staff_id)

@pytest.mark.asyncio
async def test_create_staff(staff_repository, mock_db_session):
    # Arrange
    staff_data = Staff(username="newuser")

    # Act
    result = await staff_repository.create_staff(staff_data)

    # Assert
    assert result == staff_data
    mock_db_session.add.assert_called_once_with(staff_data)
    mock_db_session.flush.assert_called_once()
