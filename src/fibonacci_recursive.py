def fibonacci_recursive(n):
    """
    Generate the nth Fibonacci number using recursion.

    Args:
        n (int): The position of the Fibonacci number to generate.
               Follows 1-based indexing (1st Fibonacci number is 1).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(2)
        1
        >>> fibonacci_recursive(3)
        2
        >>> fibonacci_recursive(6)
        8
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle invalid input
    if n < 1:
        raise ValueError("n must be a positive integer (≥ 1)")
    
    # Base cases for first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1
    
    # Recursive case: sum of two previous Fibonacci numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)