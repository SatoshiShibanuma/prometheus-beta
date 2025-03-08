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
    
    # Helper to get all subsequences of specific parity
    def extract_parity_subsequences(parity_check):
        subsequences = []
        current_sub = []
        
        for num in arr:
            if parity_check(num):
                current_sub.append(num)
            else:
                if current_sub:
                    subsequences.append(current_sub)
                current_sub = []
        
        # Add last subsequence if it exists
        if current_sub:
            subsequences.append(current_sub)
        
        return max(subsequences, key=len) if subsequences else []
    
    # Extract both odd and even subsequences
    odd_subs = extract_parity_subsequences(lambda x: x % 2 != 0)
    even_subs = extract_parity_subsequences(lambda x: x % 2 == 0)
    
    # Prioritize odd subsequence if lengths are equal or longer
    return odd_subs if len(odd_subs) >= len(even_subs) else even_subs