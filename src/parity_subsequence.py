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
    
    def find_fullest_subsequence(parity_check):
        """
        Find the fullest possible subsequence of a specific parity.
        Ensures we can extract a full line of odd or even numbers.
        """
        max_subs = []
        current_length = 0
        best_length = 0
        candidates = []
        
        for num in arr:
            if parity_check(num):
                current_length += 1
                if current_length > best_length:
                    best_length = current_length
                    candidates = [num]
                elif current_length == best_length:
                    candidates.append(num)
            else:
                current_length = 0
        
        # Find the subsequence with maximal even/odd terms
        def get_subsequence_with_maximal_terms(start_candidate):
            subsequence = [start_candidate]
            start_idx = arr.index(start_candidate)
            
            # Try forward
            forward_idx = start_idx + 1
            while forward_idx < len(arr):
                if parity_check(arr[forward_idx]):
                    subsequence.append(arr[forward_idx])
                else:
                    break
                forward_idx += 1
            
            # Try backward
            backward_idx = start_idx - 1
            while backward_idx >= 0:
                if parity_check(arr[backward_idx]):
                    subsequence.insert(0, arr[backward_idx])
                else:
                    break
                backward_idx -= 1
            
            return subsequence
        
        return max(
            [get_subsequence_with_maximal_terms(candidate) for candidate in candidates],
            key=len
        )
    
    # Compute and compare subsequences
    odd_subsequence = find_fullest_subsequence(lambda x: x % 2 != 0)
    even_subsequence = find_fullest_subsequence(lambda x: x % 2 == 0)
    
    # Prefer odd subsequence if equal or longer
    return odd_subsequence if len(odd_subsequence) >= len(even_subsequence) else even_subsequence