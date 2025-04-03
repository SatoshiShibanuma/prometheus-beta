def find_palindrome_pairs(words):
    """
    Find indices of word pairs that form palindromes when concatenated.
    
    Args:
        words (list): A list of strings to check for palindrome pairs
    
    Returns:
        list: A list of pairs of indices where concatenated words form palindromes
    
    Time Complexity: O(n^2 * m), where n is the number of words and m is word length
    Space Complexity: O(n^2)
    
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
            concat = words[i] + words[j]
            
            # Check if concatenated pair forms a palindrome
            if is_palindrome(concat):
                result.append([i, j])
    
    return result