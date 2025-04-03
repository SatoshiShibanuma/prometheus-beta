import pytest
from src.anagram_finder import find_anagrams

def test_basic_anagram_finding():
    """Test finding anagrams in a simple list"""
    word = "listen"
    word_list = ["silent", "enlist", "google", "inlets"]
    assert set(find_anagrams(word, word_list)) == {"silent", "enlist", "inlets"}

def test_case_insensitive():
    """Test that anagram finding is case-insensitive"""
    word = "Listen"
    word_list = ["SILENT", "Enlist", "google", "Inlets"]
    assert set(find_anagrams(word, word_list)) == {"SILENT", "Enlist", "Inlets"}

def test_no_anagrams():
    """Test when no anagrams are found"""
    word = "python"
    word_list = ["java", "cpp", "rust"]
    assert find_anagrams(word, word_list) == []

def test_word_not_included_in_result():
    """Test that the original word is not included in the result"""
    word = "listen"
    word_list = ["silent", "listen", "enlist"]
    assert set(find_anagrams(word, word_list)) == {"silent", "enlist"}

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input word must be a string"):
        find_anagrams(123, ["test"])
    
    with pytest.raises(TypeError, match="Word list must be a list"):
        find_anagrams("test", "not a list")

def test_empty_string():
    """Test handling of empty string input"""
    with pytest.raises(ValueError, match="Word cannot be an empty string"):
        find_anagrams("", ["test"])
    with pytest.raises(ValueError, match="Word cannot be an empty string"):
        find_anagrams("   ", ["test"])

def test_whitespace_handling():
    """Test handling of whitespace in words"""
    word = " listen "
    word_list = ["silent ", " enlist", "google"]
    assert set(find_anagrams(word, word_list)) == {"silent", "enlist"}

def test_empty_word_list():
    """Test finding anagrams in an empty list"""
    word = "test"
    assert find_anagrams(word, []) == []