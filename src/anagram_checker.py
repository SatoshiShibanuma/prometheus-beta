def anagram_checker(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word,
    using all the original letters exactly once.

    Args:
        word1 (str): The first word to compare
        word2 (str): The second word to compare

    Returns:
        bool: True if the words are anagrams, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Validate input
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Inputs must be strings")
    
    # Remove whitespace and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check for empty strings
    if not word1 or not word2:
        raise ValueError("Input strings cannot be empty")
    
    # Compare sorted character lists
    return sorted(word1) == sorted(word2)