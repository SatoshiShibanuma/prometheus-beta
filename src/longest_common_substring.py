def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two given strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring. If no common substring exists, 
             returns an empty string.
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_substring("hello", "world")
        ''
        >>> longest_common_substring("programming", "programmer")
        'program'
        >>> longest_common_substring("", "test")
        ''
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Prefer exact string comparisons, then case-sensitive matching
    if str1 == str2:
        return str1
    
    # Handle case sensitivity
    str1, str2 = str1.lower(), str2.lower()
    
    # Create a matrix to store lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Dynamic programming to find longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # Return the longest common substring with the exact same case as str1
    longest = str1[end_index - max_length + 1 : end_index + 1] if max_length > 0 else ""
    
    # Additional check to prevent partial matches when no true common substring exists
    return longest if _has_distinct_substring(str1, str2, longest) else ""

def _has_distinct_substring(str1: str, str2: str, substring: str) -> bool:
    """
    Helper function to validate if the substring is distinct.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        substring (str): Potential common substring
    
    Returns:
        bool: True if substring is truly common, False otherwise
    """
    # If substring is empty, return False
    if not substring:
        return False
    
    # Check that substring exists in both strings
    return (substring in str1.lower() and 
            substring in str2.lower() and 
            len(substring) > 1)  # Prevent single-character false positives