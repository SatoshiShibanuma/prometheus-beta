def compute_fibonacci(n):
    """
    Compute the nth Fibonacci number using an efficient dynamic programming approach.
    
    This function uses bottom-up dynamic programming to calculate the nth Fibonacci number
    with O(n) time complexity and O(1) space complexity.
    
    Args:
        n (int): The index of the Fibonacci number to compute (non-negative integer)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If the input is a negative number
        TypeError: If the input is not an integer
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n <= 1:
        return n
    
    # Use dynamic programming with constant space
    prev, curr = 0, 1
    
    # Iterate to compute nth Fibonacci number
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr