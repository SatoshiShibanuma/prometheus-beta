def find_palindrome_pairs(words):
    """
    Find all pairs of indices where concatenated strings form a palindrome.
    
    Args:
        words (list): A list of strings to check for palindrome pairs.
    
    Returns:
        list: A list of tuples containing pairs of indices where 
              words[i] + words[j] or words[j] + words[i] form a palindrome.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-string elements.
    
    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [(0, 1), (1, 0)]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [(0, 1), (1, 0), (2, 4), (3, 2)]
    """
    # Input validation
    if not isinstance(words, list):
        raise TypeError("Input must be a list of strings")
    
    if any(not isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    # Store palindrome pairs
    palindrome_pairs = []
    
    # Check all possible pairs
    for i in range(len(words)):
        for j in range(len(words)):
            # Skip same index
            if i == j:
                continue
            
            # Check if concatenation forms a palindrome
            if is_palindrome(words[i] + words[j]):
                palindrome_pairs.append((i, j))
    
    return palindrome_pairs

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Args:
        s (str): String to check.
    
    Returns:
        bool: True if string is a palindrome, False otherwise.
    """
    return s == s[::-1]