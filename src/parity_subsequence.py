def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Retains original sequence order and uses maximal matching elements.
    
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
    
    def compute_subsequence(parity_check):
        subsequence = []
        # Strategy: find contiguous subsequence starting at first matching element
        for start in range(len(arr)):
            if parity_check(arr[start]):
                current = [arr[start]]
                # Check forward
                for j in range(start + 1, len(arr)):
                    if parity_check(arr[j]) and abs(arr[j] - current[-1]) <= 1:
                        current.append(arr[j])
                
                # Compare with found subsequence
                subsequence = max(subsequence, current, key=len)
        
        return subsequence
    
    # Compute subsequences
    odd_subsequence = compute_subsequence(lambda x: x % 2 != 0)
    even_subsequence = compute_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd subsequence if equal or longer
    return odd_subsequence if len(odd_subsequence) >= len(even_subsequence) else even_subsequence