def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Prioritizes odd subsequence when selecting subsequences.
    
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
    
    def max_parity_subsequence(parity_check):
        candidates = []
        start_indices = [i for i, num in enumerate(arr) if parity_check(num)]
        
        for start_index in start_indices:
            subsequence = [arr[start_index]]
            
            # Check forward
            for j in range(start_index + 1, len(arr)):
                if parity_check(arr[j]):
                    subsequence.append(arr[j])
                else:
                    break
            
            # Check backward
            for j in range(start_index - 1, -1, -1):
                if parity_check(arr[j]):
                    subsequence.insert(0, arr[j])
                else:
                    break
            
            candidates.append(subsequence)
        
        return max(candidates, key=len, default=[])
    
    # Compute subsequences
    odd_sub = max_parity_subsequence(lambda x: x % 2 != 0)
    even_sub = max_parity_subsequence(lambda x: x % 2 == 0)
    
    # Return odd subsequence if lengths are equal or longer
    return odd_sub if len(odd_sub) >= len(even_sub) else even_sub