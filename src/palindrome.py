def is_palindrome(s: str) -> bool:
    """
    Determine if a given string is a palindrome, ignoring spaces, punctuation, and case.
    
    A palindrome reads the same backward as forward when considering only alphanumeric characters.
    
    Args:
        s (str): The input string to check for palindrome properties.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same backward and forward
    return cleaned == cleaned[::-1]