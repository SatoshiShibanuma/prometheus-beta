import random

def convert_to_random_case(input_string):
    """
    Convert a string to random case by randomly capitalizing each character.
    
    Args:
        input_string (str): The input string to be converted to random case.
    
    Returns:
        str: A new string with each character randomly capitalized.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )