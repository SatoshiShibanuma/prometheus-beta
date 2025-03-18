import logging
import sys
from typing import Any, Dict, Optional

def log_api_response_payload_size(response: Dict[str, Any], 
                                   logger: Optional[logging.Logger] = None,
                                   log_level: int = logging.INFO) -> int:
    """
    Log the size of an API response payload.

    Args:
        response (Dict[str, Any]): The API response dictionary to measure.
        logger (Optional[logging.Logger], optional): Logger to use. 
                Defaults to creating a new logger.
        log_level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        int: Size of the payload in bytes.

    Raises:
        TypeError: If response is not a dictionary.
        ValueError: If response is empty.
    """
    # Validate input
    if not isinstance(response, dict):
        raise TypeError("Response must be a dictionary")
    
    if not response:
        raise ValueError("Response cannot be empty")

    # Use provided logger or create a default one
    if logger is None:
        logger = logging.getLogger(__name__)
        # If no handlers, add a default handler
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)

    # Calculate payload size
    try:
        import sys
        import json
        
        # Convert response to JSON to get consistent size measurement
        payload_json = json.dumps(response)
        payload_size = sys.getsizeof(payload_json)

        # Log the payload size
        logger.log(log_level, f"API Response Payload Size: {payload_size} bytes")

        return payload_size

    except Exception as e:
        logger.error(f"Error calculating payload size: {str(e)}")
        raise