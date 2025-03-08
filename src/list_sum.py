def find_smallest_list_sum(list1, list2):
    """
    Find the smallest possible sum between two lists of integers.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    
    Returns:
        int: The smallest possible sum that can be formed by 
             selecting one number from each list
    
    Raises:
        ValueError: If either input is not a list or contains non-integer elements
        ValueError: If either list is empty
    """
    # Input validation
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    
    if not list1 or not list2:
        raise ValueError("Lists cannot be empty")
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in list1 + list2):
        raise ValueError("All list elements must be integers")
    
    # Find the smallest sum by selecting the values that result in the smallest sum
    return min(x + y for x in list1 for y in list2)