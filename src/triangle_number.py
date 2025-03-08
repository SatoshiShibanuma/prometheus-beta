def triangle_number(num):
    """
    Determine if a number is a Triangle Number.
    
    A Triangle Number is a number that can be represented as the sum of its proper divisors.
    Proper divisors are positive integers that evenly divide the number, excluding the number itself.
    
    Args:
        num (int): The number to check for being a Triangle Number.
    
    Returns:
        bool: True if the number is a Triangle Number, False otherwise.
    
    Raises:
        ValueError: If the input is not a positive integer.
    
    Examples:
        >>> triangle_number(6)  # 6 is a Triangle Number (1 + 2 + 3 = 6)
        True
        >>> triangle_number(10)  # 10 is a Triangle Number (1 + 2 + 3 + 4 = 10)
        True
        >>> triangle_number(12)  # 12 is not a Triangle Number
        False
    """
    # Validate input
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if num == 1:
        return True
    
    # Find proper divisors
    proper_divisors = [i for i in range(1, num) if num % i == 0]
    
    # Sum the proper divisors
    divisor_sum = sum(proper_divisors)
    
    # Check if the sum of proper divisors equals the original number
    return divisor_sum == num