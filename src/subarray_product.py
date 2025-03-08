def count_subarrays_with_product_less_than_k(nums, k):
    """
    Calculate the number of subarrays where the product of elements is less than k.
    
    Args:
        nums (List[int]): Input array of positive integers
        k (int): Upper bound for subarray product
    
    Returns:
        int: Number of subarrays with product less than k
    
    Raises:
        ValueError: If k is less than or equal to 0
        TypeError: If inputs are not of the correct type
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Validate inputs
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    # Handle edge cases
    if not nums:
        return 0
    
    count = 0
    left = 0
    curr_product = 1
    
    for right in range(len(nums)):
        # Expand the window by multiplying current element
        curr_product *= nums[right]
        
        # Shrink the window from the left if product exceeds k
        while left <= right and curr_product >= k:
            curr_product //= nums[left]
            left += 1
        
        # Count subarrays ending at current right index
        count += right - left + 1
    
    return count