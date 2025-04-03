def find_anagrams(word, word_list):
    """
    Find all anagrams of a given word within a list of words.
    
    An anagram is a word that contains exactly the same characters as another word,
    just in a different order. The function is case-insensitive.
    
    Args:
        word (str): The word to find anagrams for
        word_list (list): A list of words to search for anagrams
    
    Returns:
        list: A list of anagrams found in the word_list
    
    Raises:
        TypeError: If word is not a string or word_list is not a list
        ValueError: If word is an empty string after stripping
    """
    # Input validation
    if not isinstance(word, str):
        raise TypeError("Input word must be a string")
    if not isinstance(word_list, list):
        raise TypeError("Word list must be a list")
    
    # Normalize input
    word = word.lower().strip()
    
    # Validate word
    if not word:
        raise ValueError("Word cannot be an empty string")
    
    # Sort the characters of the input word
    sorted_word = ''.join(sorted(word))
    
    # Find anagrams (excluding the original word)
    anagrams = [
        w.strip() for w in word_list 
        if w.strip().lower() != word and 
        ''.join(sorted(w.strip().lower())) == sorted_word
    ]
    
    return anagrams