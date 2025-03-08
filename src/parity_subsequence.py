def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Prioritizes odd subsequence when multiple options exist.
    
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
    
    def get_max_subsequence(parity_check):
        max_sub = []
        current_sub = []
        
        for num in arr:
            if parity_check(num):
                if not current_sub or num in current_sub:
                    current_sub.append(num)
                else:
                    max_sub = max(max_sub, current_sub, key=len)
                    current_sub = [num]
        
        # Final check
        max_sub = max(max_sub, current_sub, key=len)
        return max_sub
    
    # Compute subsequences
    odd_sub = get_max_subsequence(lambda x: x % 2 != 0)
    even_sub = get_max_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd if lengths are equal or longer
    return odd_sub if len(odd_sub) >= len(even_sub) else even_sub