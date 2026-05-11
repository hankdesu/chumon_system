import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlmodel import select
from app.repositories.meal_repository import MealRepository
from app.models.meal import Meal
from app.dtos.query_params import PaginationParams, OrderParams, FilterParams

@pytest.fixture
def mock_db_session():
    mock = AsyncMock()
    mock.add = MagicMock()  # add is synchronous
    return mock

@pytest.fixture
def meal_repository(mock_db_session):
    return MealRepository(db_session=mock_db_session)

@pytest.mark.asyncio
async def test_get_meals(meal_repository, mock_db_session):
    # Arrange
    page_params = PaginationParams(limit=10, offset=0)
    order_params = OrderParams(sort_by="name", order="asc")
    filter_params = FilterParams(query="test")
    
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [Meal(id=1, name="Test Meal")]
    mock_db_session.execute.return_value = mock_result

    # Act
    result = await meal_repository.get_meals(page_params, order_params, filter_params)

    # Assert
    assert len(result) == 1
    assert result[0].name == "Test Meal"
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_get_meals_default_sort(meal_repository, mock_db_session):
    # Arrange
    page_params = PaginationParams(limit=10, offset=0)
    order_params = OrderParams(sort_by="invalid_column", order="asc")
    filter_params = FilterParams(query=None)
    
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_db_session.execute.return_value = mock_result

    # Act
    await meal_repository.get_meals(page_params, order_params, filter_params)

    # Assert
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_get_meals_desc_order(meal_repository, mock_db_session):
    # Arrange
    page_params = PaginationParams(limit=10, offset=0)
    order_params = OrderParams(sort_by="name", order="desc")
    filter_params = FilterParams(query=None)
    
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_db_session.execute.return_value = mock_result

    # Act
    await meal_repository.get_meals(page_params, order_params, filter_params)

    # Assert
    mock_db_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_get_meal_by_id(meal_repository, mock_db_session):
    # Arrange
    meal_id = 1
    expected_meal = Meal(id=meal_id, name="Test Meal")
    mock_db_session.get.return_value = expected_meal

    # Act
    result = await meal_repository.get_meal_by_id(meal_id)

    # Assert
    assert result == expected_meal
    mock_db_session.get.assert_called_once_with(Meal, meal_id)

@pytest.mark.asyncio
async def test_create_meal(meal_repository, mock_db_session):
    # Arrange
    meal_data = Meal(name="New Meal")

    # Act
    result = await meal_repository.create_meal(meal_data)

    # Assert
    assert result == meal_data
    mock_db_session.add.assert_called_once_with(meal_data)
    mock_db_session.flush.assert_called_once()

@pytest.mark.asyncio
async def test_patch_meal(meal_repository, mock_db_session):
    # Arrange
    meal_data = Meal(id=1, name="Updated Meal")

    # Act
    result = await meal_repository.patch_meal(meal_data)

    # Assert
    assert result == meal_data
    mock_db_session.add.assert_called_once_with(meal_data)
    mock_db_session.flush.assert_called_once()
