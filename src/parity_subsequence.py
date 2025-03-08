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
    
    # Find the longest subsequence of even numbers
    def get_parity_subsequence(parity_checker):
        max_subsequence = []
        current_subsequence = []
        
        for num in arr:
            # If current number matches the parity
            if parity_checker(num):
                current_subsequence.append(num)
            else:
                # Update max_subsequence if current is longer
                if len(current_subsequence) > len(max_subsequence):
                    max_subsequence = current_subsequence.copy()
                current_subsequence = []
        
        # Check one last time after loop completes
        if len(current_subsequence) > len(max_subsequence):
            max_subsequence = current_subsequence
        
        return max_subsequence

    # Check which subsequence is longer: even or odd
    even_subsequence = get_parity_subsequence(lambda x: x % 2 == 0)
    odd_subsequence = get_parity_subsequence(lambda x: x % 2 != 0)
    
    return max(even_subsequence, odd_subsequence, key=len)