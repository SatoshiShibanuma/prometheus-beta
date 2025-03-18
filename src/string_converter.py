def convert_to_alternating_snake_case(input_string: str) -> str:
    """
    Convert a given string to alternating snake case.
    
    Alternating snake case means:
    - Convert to lowercase
    - Separate words by underscores
    - Alternate case between lowercase and uppercase words
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating snake case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> convert_to_alternating_snake_case("Hello World")
        'hello_World'
        >>> convert_to_alternating_snake_case("PYTHON PROGRAMMING")
        'python_PROGRAMMING'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string.strip():
        return ""
    
    # Split the string into words and strip
    words = [word.strip() for word in input_string.split()]
    
    # Return immediately if no words
    if not words:
        return ""
    
    # Convert the first word to lowercase
    result_words = [words[0].lower()]
    
    # Alternate case for subsequent words
    for i, word in enumerate(words[1:], 1):
        result_words.append(word.upper() if i % 2 == 1 else word.lower())
    
    # Join words with underscores
    return '_'.join(result_words)