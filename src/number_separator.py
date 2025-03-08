from typing import List, Tuple

def separate_evens_odds(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Separate a list of integers into two lists: even and odd numbers.

    Args:
        numbers (List[int]): Input list of integers to be separated.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists - 
        first list with even numbers, second list with odd numbers.

    Examples:
        >>> separate_evens_odds([1, 2, 3, 4, 5, 6])
        ([2, 4, 6], [1, 3, 5])
        >>> separate_evens_odds([])
        ([], [])
    """
    # Handle None or non-list input
    if numbers is None:
        return [], []
    
    # Separate even and odd numbers
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    
    return evens, odds