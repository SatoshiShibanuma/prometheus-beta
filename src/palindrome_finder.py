def find_palindromic_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a contiguous sequence of characters 
    that reads the same backward as forward.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of all unique palindromic substrings found in the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    # Check palindromes for each possible center
    for i in range(len(s)):
        # Odd length palindromes
        expand_around_center(i, i)
        
        # Even length palindromes
        expand_around_center(i, i+1)
    
    return list(palindromes)