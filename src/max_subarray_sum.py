def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray of length k in the given array.

    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a contiguous subarray of length k

    Raises:
        ValueError: If k is less than 1 or greater than the array length
        TypeError: If input is not a list or k is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not isinstance(k, int):
        raise TypeError("Subarray length must be an integer")
    
    # Check array and k constraints
    if k < 1:
        raise ValueError("Subarray length must be at least 1")
    
    if k > len(arr):
        raise ValueError("Subarray length cannot be larger than array length")
    
    # Handle empty array case
    if not arr:
        return 0
    
    # Sliding window approach
    # First, compute sum of first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove first element of previous window and add next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum