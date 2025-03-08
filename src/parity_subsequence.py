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
        # Tracks the valid subsequences of the specified parity
        best_sub = []
        current_sub = []
        
        for num in arr:
            # If the number matches parity
            if parity_check(num):
                # If first number or consecutive to last number
                if not current_sub or (current_sub and abs(num - current_sub[-1]) <= 1):
                    current_sub.append(num)
                else:
                    # Update best subsequence if current is longer
                    best_sub = max(best_sub, current_sub, key=len)
                    current_sub = [num]
        
        # Final check and return
        return max(best_sub, current_sub, key=len)
    
    # Compute odd and even subsequences
    odd_sub = extract_parity_subsequence(lambda x: x % 2 != 0)
    even_sub = extract_parity_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd subsequence if equal or longer
    return odd_sub if len(odd_sub) >= len(even_sub) else even_sub