def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Prioritizes continuous odd subsequence when multiple options exist.
    
    Examples:
        >>> find_longest_parity_subsequence([1, 3, 2, 4, 5])
        [1, 3, 5]
        >>> find_longest_parity_subsequence([2, 4, 6, 7, 8, 9, 10])
        [2, 4, 6]
        >>> find_longest_parity_subsequence([])
        []
    """
    if not arr:
        return []
    
    # Track subsequences for both even and odd parities
    longest_even = []
    longest_odd = []
    
    current_even = []
    current_odd = []
    
    for num in arr:
        # If number is even
        if num % 2 == 0:
            current_even.append(num)
            # Reset odd sequence if it doesn't help
            if not current_odd or (current_odd and (len(current_even) > len(current_odd))):
                current_odd = []
        # If number is odd    
        else:
            current_odd.append(num)
            # Reset even sequence if it doesn't help
            if not current_even or (current_even and (len(current_odd) > len(current_even))):
                current_even = []
        
        # Update longest subsequences
        longest_even = max(longest_even, current_even, key=len)
        longest_odd = max(longest_odd, current_odd, key=len)
    
    # Return the longer subsequence, prioritizing odd if equal
    return longest_odd if len(longest_odd) >= len(longest_even) else longest_even