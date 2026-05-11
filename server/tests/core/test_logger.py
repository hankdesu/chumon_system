import logging
from unittest.mock import MagicMock, patch, call
from app.core.logger import setup_logging

def test_setup_logging():
    mock_logger = MagicMock()
    mock_handler = MagicMock()
    mock_logger.handlers = [mock_handler]
    
    with patch("logging.getLogger", return_value=mock_logger) as mock_get_logger:
        setup_logging()
        
        # Check if setFormatter was called on the handler
        assert mock_handler.setFormatter.called
        
        # Check if it was called for the expected loggers
        expected_calls = [
            call("uvicorn"),
            call("uvicorn.error"),
            call("uvicorn.access")
        ]
        mock_get_logger.assert_has_calls(expected_calls, any_order=True)
