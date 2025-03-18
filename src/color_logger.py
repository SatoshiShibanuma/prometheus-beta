import sys
from typing import Optional, Literal

# ANSI color codes
COLOR_CODES = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

def log_colored_message(
    message: str, 
    color: Optional[Literal['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']] = None, 
    file=sys.stdout
) -> None:
    """
    Log a message in a specified color to the given output stream.

    Args:
        message (str): The message to be logged.
        color (Optional[str]): The color to use for the message. 
            Must be one of: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
            If None, logs in default color.
        file (file-like object, optional): The output stream to write to. 
            Defaults to sys.stdout.

    Raises:
        ValueError: If an invalid color is provided.
    """
    # Validate input
    if message is None:
        raise ValueError("Message cannot be None")
    
    # If no color specified, print as-is
    if color is None:
        print(message, file=file)
        return
    
    # Validate color
    if color not in COLOR_CODES:
        raise ValueError(f"Invalid color. Must be one of {list(COLOR_CODES.keys())[:-1]}")
    
    # Print colored message
    try:
        colored_message = f"{COLOR_CODES[color]}{message}{COLOR_CODES['reset']}"
        print(colored_message, file=file)
    except Exception as e:
        raise RuntimeError(f"Error printing colored message: {e}")