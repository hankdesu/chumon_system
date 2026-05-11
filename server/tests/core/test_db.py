import pytest
from unittest.mock import AsyncMock, patch
from app.core.db import get_db_session

@pytest.mark.asyncio
async def test_get_db_session_success():
    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    # We need to mock the AsyncSession constructor
    with patch("app.core.db.AsyncSession", return_value=mock_session):
        # get_db_session is an async generator
        generator = get_db_session()
        session = await anext(generator)
        
        assert session == mock_session
        
        # Close the generator
        try:
            await anext(generator)
        except StopAsyncIteration:
            pass
            
    mock_session.__aenter__.assert_called_once()
    mock_session.__aexit__.assert_called_once()

@pytest.mark.asyncio
async def test_get_db_session_exception():
    mock_session = AsyncMock()
    mock_session.__aenter__.return_value = mock_session
    mock_session.rollback = AsyncMock()
    
    with patch("app.core.db.AsyncSession", return_value=mock_session):
        generator = get_db_session()
        session = await anext(generator)
        
        assert session == mock_session
        
        # Simulate an exception during session usage
        with pytest.raises(RuntimeError):
            await generator.athrow(RuntimeError("Test error"))
            
    mock_session.rollback.assert_called_once()
    mock_session.__aexit__.assert_called_once()
