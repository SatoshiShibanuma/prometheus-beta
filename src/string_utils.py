def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a substring within a given string.

    Args:
        s (str): The input string to modify.
        start (int): The starting index of the substring to reverse (inclusive).
        end (int): The ending index of the substring to reverse (exclusive).

    Returns:
        str: A new string with the specified substring reversed.

    Raises:
        ValueError: If start or end indices are out of bounds.
        ValueError: If start index is greater than end index.
    """
    # Validate input indices
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")
    
    # If start and end are the same, return the original string
    if start == end:
        return s
    
    # Create the modified string
    modified = s[:start] + s[start:end][::-1] + s[end:]
    
    return modified