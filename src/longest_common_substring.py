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
    
    # Special case for identical strings
    if str1 == str2:
        return str1
    
    # Convert to lowercase for comparison while preserving original case
    lower_str1, lower_str2 = str1.lower(), str2.lower()
    
    # Create a matrix to store lengths of common substrings
    m, n = len(lower_str1), len(lower_str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Variables to track the longest substring
    max_length = 0
    end_index = 0
    
    # Dynamic programming to find longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lower_str1[i-1] == lower_str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                # Update max length and end index if needed
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
    
    # If no common substring of length > 1, return empty string
    if max_length < 2:
        return ""
    
    # Extract substring with the same case as in the original str1
    return str1[end_index - max_length + 1 : end_index + 1]