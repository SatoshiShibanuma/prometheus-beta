def find_palindrome_pairs(words):
    """
    Find indices of word pairs that form palindromes when concatenated.
    
    Args:
        words (list): A list of strings to check for palindrome pairs
    
    Returns:
        list: A list of pairs of indices where concatenated words form palindromes
    
    Time Complexity: O(n^2 * m), where n is the number of words and m is word length
    Space Complexity: O(1)
    
    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [[0, 1], [1, 0]]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 4], [4, 3]]
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            # Skip same index
            if i == j:
                continue
            
            # Concatenate words in both orders
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            # Check both concatenation orders
            if is_palindrome(concat1):
                result.append([i, j])
            if is_palindrome(concat2):
                result.append([j, i])
    
    # Remove duplicates while preserving order
    return list(map(list, set(map(tuple, result))))