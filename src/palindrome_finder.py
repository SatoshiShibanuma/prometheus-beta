def contains_palindrome_word(input_string: str) -> bool:
    """
    Determine if the input string contains a palindrome word.
    
    A palindrome word is a word that reads the same backward as forward.
    Ignores case and strips out non-alphanumeric characters.
    
    Args:
        input_string (str): A string containing words, numbers, and special characters
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise
    
    Examples:
        >>> contains_palindrome_word("Hello radar world")
        True
        >>> contains_palindrome_word("python is awesome")
        False
    """
    # Split the input string into words
    words = input_string.lower().split()
    
    # Check each word for palindrome
    for word in words:
        # Remove non-alphanumeric characters
        cleaned_word = ''.join(char for char in word if char.isalnum())
        
        # Check if the cleaned word is a palindrome
        if cleaned_word == cleaned_word[::-1] and len(cleaned_word) > 0:
            return True
    
    return False