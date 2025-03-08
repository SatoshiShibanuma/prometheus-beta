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
    
    def candidate_subsequences(parity_check):
        """Generate candidate subsequences for a specific parity."""
        candidates = []
        for start in range(len(arr)):
            if parity_check(arr[start]):
                # Try extending the subsequence
                current = [arr[start]]
                for next_idx in range(start + 1, len(arr)):
                    if parity_check(arr[next_idx]):
                        current.append(arr[next_idx])
                candidates.append(current)
        return max(candidates, key=len) if candidates else []
    
    # Get all subsequence candidates
    odd_subsequence = candidate_subsequences(lambda x: x % 2 != 0)
    even_subsequence = candidate_subsequences(lambda x: x % 2 == 0)
    
    # Return odd subsequence if lengths are equal or longer
    return odd_subsequence if len(odd_subsequence) >= len(even_subsequence) else even_subsequence