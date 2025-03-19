def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with at least k elements 
    and sum greater than or equal to s.

    Args:
        A (list): Input array of integers
        k (int): Minimum number of elements in the subarray
        s (int): Minimum sum threshold for the subarray

    Returns:
        int: Maximum sum of a subarray meeting the constraints, 
             or None if no such subarray exists

    Raises:
        ValueError: If input parameters are invalid
    """
    # Validate input parameters
    if not isinstance(A, list):
        raise ValueError("Input A must be a list")
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if not isinstance(s, int):
        raise ValueError("s must be an integer")
    
    # If array is too short to meet k constraint
    if len(A) < k:
        return None
    
    # Initialize variables for sliding window approach
    n = len(A)
    max_sum = None
    
    # Try all possible subarrays with at least k elements
    for start in range(n - k + 1):
        current_sum = 0
        # Extend window to cover at least k elements and find max sum
        for end in range(start, n):
            current_sum += A[end]
            
            # Check if current window meets constraints
            if (end - start + 1 >= k) and (current_sum >= s):
                if max_sum is None or current_sum > max_sum:
                    max_sum = current_sum
    
    return max_sum