from datetime import datetime

def convert_timestamp_to_readable_date(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)

    Returns:
        str: Formatted date string in the format 'Month Day, Year'

    Raises:
        TypeError: If timestamp is not a number
        ValueError: If timestamp is negative
    """
    # Validate input
    if not isinstance(timestamp, (int, float)):
        raise TypeError("Timestamp must be a number")
    
    if timestamp < 0:
        raise ValueError("Timestamp cannot be negative")
    
    # Convert timestamp to datetime object
    try:
        date = datetime.fromtimestamp(timestamp)
    except (ValueError, OSError):
        raise ValueError("Invalid timestamp value")
    
    # Format the date in a human-readable format
    return date.strftime("%B %d, %Y")