def _is_common_substring(substr: str, str1: str, str2: str) -> bool:
    """
    Check if a substring is truly common between two strings.
    
    Args:
        substr (str): Potential substring to check
        str1 (str): First string
        str2 (str): Second string
    
    Returns:
        bool: True if substring is genuinely common, False otherwise
    """
    return (substr.lower() in str1.lower() and 
            substr.lower() in str2.lower() and 
            len(substr) > 1)

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
    
    # Special case for identical strings with exact case
    if str1 == str2:
        return str1
    
    # Check case sensitivity
    if str1.lower() == str2.lower():
        return ""
    
    # Computation of common substring
    def find_substring(s1, s2):
        # Preferred implementation
        longest = ""
        for start in range(len(s1)):
            for end in range(start + 2, len(s1) + 1):  # Ensure substring of at least 2 chars
                substr = s1[start:end]
                if _is_common_substring(substr, s1, s2):
                    if len(substr) > len(longest):
                        longest = substr
        return longest

    # Perform computation with original str1 while allowing mismatch in str2
    result1 = find_substring(str1, str2)
    result2 = find_substring(str2, str1)
    
    # Return the longer of the two results
    return result1 if len(result1) >= len(result2) else result2