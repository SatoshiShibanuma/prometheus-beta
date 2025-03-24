import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation criteria:
    - Must have a local part (before @)
    - Must have a domain part (after @)
    - Local part can contain letters, digits, and some special characters
    - Domain part must have at least one dot
    - Total length should be between 3 and 254 characters
    """
    # Check if email is a string and has valid length
    if not isinstance(email, str):
        return False
    
    # Check overall email length (RFC 5321)
    if len(email) < 3 or len(email) > 254:
        return False
    
    # Regular expression for email validation
    # This regex covers most common email format requirements
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the regex pattern
    if not re.match(email_regex, email):
        return False
    
    return True