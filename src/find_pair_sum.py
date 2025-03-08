def find_pairs_with_target_sum(arr, target_sum):
    """
    Find all unique pairs of numbers in an array that add up to a target sum.

    Args:
        arr (list): A list of unique integers
        target_sum (int): The target sum to find pairs for

    Returns:
        list: A list of tuples containing pairs of numbers that sum to the target

    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If input list contains duplicate elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(target_sum, int):
        raise TypeError("Target sum must be an integer")
    
    # Check for duplicates
    if len(arr) != len(set(arr)):
        raise ValueError("Input array must contain unique elements")

    # Require at least two elements for a pair
    if len(arr) < 2:
        return []

    # Use a hash set for efficient lookup
    seen = set()
    result = []

    for num in arr:
        complement = target_sum - num
        
        # Check if the complement exists and is not the same as current number
        if complement in seen and complement != num:
            # Ensure pairs are sorted to avoid duplicates
            pair = tuple(sorted((num, complement)))
            if pair not in result:
                result.append(pair)
        
        seen.add(num)

    return result