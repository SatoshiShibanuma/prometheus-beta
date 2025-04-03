def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order with special handling for even number squares.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted list with even number squares sorted in descending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Sort the entire array in ascending order
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_squares = [x**2 for x in sorted_arr if x % 2 == 0]
    odd_numbers = [x for x in sorted_arr if x % 2 != 0]
    
    # Sort even squares in descending order
    even_squares_desc = sorted(even_squares, reverse=True)
    
    # Combine odd numbers and descending even squares
    return odd_numbers + even_squares_desc