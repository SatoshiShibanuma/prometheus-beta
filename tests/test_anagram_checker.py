import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("triangle", "integral") == True

def test_case_insensitive():
    """Test that anagram checking is case-insensitive"""
    assert anagram_checker("Listen", "Silent") == True
    assert anagram_checker("LISTEN", "silent") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_spaces_in_words():
    """Test anagram checking with spaces"""
    assert anagram_checker("debit card", "bad credit") == True
    assert anagram_checker(" triangle ", "integral ") == True

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        anagram_checker(123, "test")
    
    with pytest.raises(TypeError):
        anagram_checker("test", None)
    
    with pytest.raises(ValueError):
        anagram_checker("", "test")
    
    with pytest.raises(ValueError):
        anagram_checker("test", "")

def test_single_character_words():
    """Test anagram checking with single-character words"""
    assert anagram_checker("a", "a") == True
    assert anagram_checker("a", "b") == False