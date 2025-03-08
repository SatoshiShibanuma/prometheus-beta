def filter_special_multiples(numbers):
    """
    Filter a list of integers to include only numbers that are multiples 
    of either 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, 
              but not multiples of both 3 and 5
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer elements
    if any(not isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    
    # Filter numbers that are multiples of 3 or 5, but not both
    special_multiples = [
        num for num in numbers 
        if (num % 3 == 0) != (num % 5 == 0)
    ]
    
    # Return sorted list
    return sorted(special_multiples)