def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        If equal lengths, prioritizes even subsequence.
    
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
    
    # Compute maximum even and odd subsequences
    def max_parity_subsequence(parity_check):
        subsequence = []
        current = []
        
        for num in arr:
            if parity_check(num):
                current.append(num)
            else:
                subsequence = max(subsequence, current, key=len)
                current = []
        
        # Check once after loop ends
        return max(subsequence, current, key=len)
    
    even_sub = max_parity_subsequence(lambda x: x % 2 == 0)
    odd_sub = max_parity_subsequence(lambda x: x % 2 != 0)
    
    # Prefer even if lengths are equal or even is longer
    return even_sub if len(even_sub) >= len(odd_sub) else odd_sub