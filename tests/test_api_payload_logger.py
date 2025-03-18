import pytest
import logging
import json
import sys
from src.api_payload_logger import log_api_response_payload_size

class MockLogger:
    def __init__(self):
        self.log_messages = []
        self.error_messages = []

    def log(self, level, msg):
        self.log_messages.append((level, msg))

    def error(self, msg):
        self.error_messages.append(msg)

def test_log_api_response_payload_size_success():
    # Test a simple response
    response = {"key": "value"}
    
    # Create a mock logger
    mock_logger = MockLogger()
    
    # Call the function
    payload_size = log_api_response_payload_size(response, logger=mock_logger)
    
    # Verify payload size is correct
    assert payload_size > 0
    
    # Verify logging occurred
    assert len(mock_logger.log_messages) == 1
    log_level, log_msg = mock_logger.log_messages[0]
    assert "API Response Payload Size" in log_msg
    assert log_level == logging.INFO

def test_log_api_response_payload_size_complex_response():
    # Test a more complex nested response
    response = {
        "users": [
            {"name": "John", "age": 30},
            {"name": "Jane", "age": 25}
        ],
        "total": 2
    }
    
    mock_logger = MockLogger()
    payload_size = log_api_response_payload_size(response, logger=mock_logger)
    
    assert payload_size > 0
    assert len(mock_logger.log_messages) == 1

def test_log_api_response_payload_size_invalid_input():
    # Test with non-dictionary input
    with pytest.raises(TypeError):
        log_api_response_payload_size("Not a dictionary")

def test_log_api_response_payload_size_empty_response():
    # Test with empty dictionary
    with pytest.raises(ValueError):
        log_api_response_payload_size({})

def test_log_api_response_payload_size_custom_log_level():
    response = {"key": "value"}
    mock_logger = MockLogger()
    
    payload_size = log_api_response_payload_size(
        response, 
        logger=mock_logger, 
        log_level=logging.DEBUG
    )
    
    # Verify that logging occurred at the specified log level
    assert len(mock_logger.log_messages) == 1
    log_level, log_msg = mock_logger.log_messages[0]
    assert log_level == logging.DEBUG