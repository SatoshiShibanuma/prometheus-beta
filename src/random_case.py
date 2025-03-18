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
    
    # Convert to random case, ensuring at least some characters change
    result = ''.join(
        char.upper() if random.random() > 0.5 else char.lower() 
        for char in input_string
    )
    
    # If result is identical to input, force at least one character change
    if result.lower() == input_string.lower():
        # Pick a random index to change
        change_index = random.randint(0, len(input_string) - 1)
        result_list = list(result)
        result_list[change_index] = result_list[change_index].swapcase()
        result = ''.join(result_list)
    
    return result