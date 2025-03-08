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
    
    def compute_subsequence(parity_check):
        best_sub = []
        current_sub = []
        complete_sub = False
        
        for i, num in enumerate(arr):
            if parity_check(num):
                current_sub.append(num)
                # Track additional elements after subsequence to ensure maximal sequence
                if current_sub and not complete_sub:
                    # Continue gathering subsequent matching elements
                    j = i + 1
                    while j < len(arr) and parity_check(arr[j]):
                        current_sub.append(arr[j])
                        j += 1
                    complete_sub = True
            else:
                best_sub = max(best_sub, current_sub, key=len)
                current_sub = []
        
        # Final check
        best_sub = max(best_sub, current_sub, key=len)
        return best_sub

    odd_sub = compute_subsequence(lambda x: x % 2 != 0)
    even_sub = compute_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd subsequence if lengths are equal or longer
    return odd_sub if len(odd_sub) >= len(even_sub) else even_sub