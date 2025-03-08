def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
    
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
    even_subs = []
    odd_subs = []
    
    current_even = []
    current_odd = []
    
    for num in arr:
        if num % 2 == 0:  # even
            current_even.append(num)
            current_odd = []
        else:  # odd
            current_odd.append(num)
            current_even = []
        
        # Update max subsequences
        even_subs = max(even_subs, current_even, key=len)
        odd_subs = max(odd_subs, current_odd, key=len)
    
    # Return the longer subsequence
    return max(even_subs, odd_subs, key=len)