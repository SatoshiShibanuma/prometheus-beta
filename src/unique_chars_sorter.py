def sort_unique_chars(input_string: str) -> list:
    """
    Take a string and return a sorted list of unique characters in case-sensitive alphabetical order.

    Args:
        input_string (str): The input string to process.

    Returns:
        list: A sorted list of unique characters from the input string.

    Examples:
        >>> sort_unique_chars("hello")
        ['e', 'h', 'l', 'o']
        >>> sort_unique_chars("Python")
        ['P', 'h', 'n', 'o', 't', 'y']
        >>> sort_unique_chars("")
        []
    """
    # Handle empty string case
    if not input_string:
        return []
    
    # Remove duplicates while preserving order, then sort
    return sorted(set(input_string), key=lambda x: x)