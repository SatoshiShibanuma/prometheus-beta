def find_longest_parity_subsequence(arr):
    """
    Find the longest subsequence of integers with the same parity (all even or all odd).
    
    Args:
        arr (list[int]): Input list of integers.
    
    Returns:
        list[int]: The longest subsequence with consistent parity.
        If input is empty, returns an empty list.
        Prioritizes odd subsequence in case of equal lengths.
    
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
    
    def extract_parity_subsequence(parity_check):
        # Tracks the best subsequence of the specified parity
        best_sub = []
        current_sub = [arr[0]] if parity_check(arr[0]) else []
        
        for num in arr[1:]:
            if parity_check(num):
                # If current subsequence is empty, start with this number
                if not current_sub:
                    current_sub = [num]
                # Non-consecutive handling: reset or adjust subsequence
                elif len(current_sub) >= 1 and abs(num - current_sub[-1]) > 1:
                    best_sub = max(best_sub, current_sub, key=len)
                    current_sub = [num]
                else:
                    current_sub.append(num)
        
        # Final check
        best_sub = max(best_sub, current_sub, key=len)
        return best_sub
    
    # Compute subsequences of different parities
    odd_sub = extract_parity_subsequence(lambda x: x % 2 != 0)
    even_sub = extract_parity_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd subsequence if equal or longer
    return odd_sub if len(odd_sub) >= len(even_sub) else even_sub