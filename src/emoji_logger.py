import logging
import emoji

def log_with_emojis(message, emoji_symbol=None, log_level='info'):
    """
    Log a message with an optional emoji symbol.

    Args:
        message (str): The message to log
        emoji_symbol (str, optional): An emoji to prepend to the message. 
                                      Can be a string or an emoji code.
        log_level (str, optional): Logging level. 
                                   Defaults to 'info'. 
                                   Options: 'debug', 'info', 'warning', 'error', 'critical'

    Returns:
        str: The logged message with emoji (if provided)

    Raises:
        ValueError: If an invalid log level is provided
        TypeError: If message is not a string
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Validate log level
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }

    if log_level.lower() not in log_levels:
        raise ValueError(f"Invalid log level. Choose from {', '.join(log_levels.keys())}")

    # Add emoji if provided
    if emoji_symbol:
        try:
            # Convert emoji code to actual emoji if needed
            formatted_emoji = emoji.emojize(emoji_symbol, language='alias') if emoji_symbol.startswith(':') else emoji_symbol
            full_message = f"{formatted_emoji} {message}"
        except Exception:
            # If emoji conversion fails, fall back to original message
            full_message = message
    else:
        full_message = message

    # Log the message
    log_func = log_levels[log_level.lower()]
    log_func(full_message)

    return full_message