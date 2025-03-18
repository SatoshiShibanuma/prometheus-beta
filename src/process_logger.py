import time
import logging
from typing import Callable, Optional, Any

class ProcessLogger:
    """
    A class to log real-time progress of a process with customizable logging options.
    
    Attributes:
        logger (logging.Logger): Logger instance for tracking process progress
        total_steps (Optional[int]): Total number of steps in the process, if known
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None, total_steps: Optional[int] = None):
        """
        Initialize the ProcessLogger.
        
        Args:
            logger (Optional[logging.Logger]): Custom logger. If None, creates a default logger.
            total_steps (Optional[int]): Total number of steps in the process, if known.
        """
        self.logger = logger or logging.getLogger(__name__)
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = None
    
    def start(self):
        """
        Mark the start of the process and log the start message.
        """
        self.start_time = time.time()
        self.logger.info("Process started")
    
    def update(self, step_increment: int = 1, message: Optional[str] = None):
        """
        Update the progress of the process.
        
        Args:
            step_increment (int): Number of steps completed. Defaults to 1.
            message (Optional[str]): Optional custom message to log with the progress.
        
        Raises:
            ValueError: If step_increment is negative.
        """
        if step_increment < 0:
            raise ValueError("Step increment must be non-negative")
        
        self.current_step += step_increment
        
        # Calculate progress percentage if total steps is known
        progress_msg = f"Progress: {self.current_step} steps"
        if self.total_steps is not None:
            try:
                progress_percentage = (self.current_step / self.total_steps) * 100
                progress_msg += f" ({progress_percentage:.2f}%)"
            except (TypeError, ZeroDivisionError):
                pass
        
        # Add custom message if provided
        if message:
            progress_msg += f" - {message}"
        
        self.logger.info(progress_msg)
    
    def complete(self, message: Optional[str] = None):
        """
        Mark the process as complete and log completion details.
        
        Args:
            message (Optional[str]): Optional custom completion message.
        """
        end_time = time.time()
        duration = end_time - self.start_time if self.start_time else 0
        
        completion_msg = "Process completed"
        if duration > 0:
            completion_msg += f" in {duration:.2f} seconds"
        
        if message:
            completion_msg += f" - {message}"
        
        self.logger.info(completion_msg)

def log_process_progress(
    func: Callable, 
    total_steps: Optional[int] = None, 
    logger: Optional[logging.Logger] = None
) -> Callable:
    """
    A decorator to automatically log progress for a function.
    
    Args:
        func (Callable): The function to be decorated
        total_steps (Optional[int]): Total number of steps in the process
        logger (Optional[logging.Logger]): Custom logger to use
    
    Returns:
        Callable: Wrapped function with progress logging
    """
    def wrapper(*args: Any, **kwargs: Any):
        process_logger = ProcessLogger(logger=logger, total_steps=total_steps)
        process_logger.start()
        
        try:
            result = func(*args, **kwargs)
            process_logger.complete()
            return result
        except Exception as e:
            process_logger.complete(f"Failed with error: {str(e)}")
            raise
    
    return wrapper