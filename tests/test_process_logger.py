import logging
import time
import pytest
from src.process_logger import ProcessLogger, log_process_progress

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(message)

def test_process_logger_basic():
    mock_logger = MockLogger()
    logger = ProcessLogger(logger=mock_logger, total_steps=10)
    
    logger.start()
    assert "Process started" in mock_logger.logs[0]
    
    logger.update()
    assert "Progress: 1 steps (10.00%)" in mock_logger.logs[1]
    
    logger.update(3)
    assert "Progress: 4 steps (40.00%)" in mock_logger.logs[2]
    
    logger.complete("Finished successfully")
    assert "Process completed" in mock_logger.logs[3]
    assert "Finished successfully" in mock_logger.logs[3]

def test_process_logger_without_total_steps():
    mock_logger = MockLogger()
    logger = ProcessLogger(logger=mock_logger)
    
    logger.start()
    logger.update(message="Initial step")
    assert "Progress: 1 steps - Initial step" in mock_logger.logs[1]

def test_process_logger_negative_step_increment():
    mock_logger = MockLogger()
    logger = ProcessLogger(logger=mock_logger)
    
    with pytest.raises(ValueError, match="Step increment must be non-negative"):
        logger.update(-1)

def test_log_process_progress_decorator():
    mock_logger = MockLogger()
    
    @log_process_progress(total_steps=3, logger=mock_logger)
    def sample_process():
        time.sleep(0.1)
        return "Success"
    
    result = sample_process()
    assert result == "Success"
    assert any("Process started" in log for log in mock_logger.logs)
    assert any("Process completed" in log for log in mock_logger.logs)

def test_log_process_progress_decorator_with_error():
    mock_logger = MockLogger()
    
    @log_process_progress(total_steps=3, logger=mock_logger)
    def failing_process():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError, match="Test error"):
        failing_process()
    
    assert any("Failed with error" in log for log in mock_logger.logs)