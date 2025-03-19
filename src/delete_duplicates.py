def deleteDuplicates(arr):
    """
    Delete all duplicate elements from the input array while maintaining the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, preserving the first occurrence of each element
    
    Examples:
        >>> deleteDuplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> deleteDuplicates([])
        []
        >>> deleteDuplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add item if it hasn't been seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result