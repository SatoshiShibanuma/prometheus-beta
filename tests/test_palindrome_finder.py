import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_basic_palindromes():
    """Test finding basic palindromic substrings."""
    result = find_palindromic_substrings("abba")
    assert set(result) == {"a", "b", "bb", "abba"}

def test_empty_string():
    """Test handling of empty string."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test string with single character."""
    result = find_palindromic_substrings("a")
    assert set(result) == {"a"}

def test_no_palindromes():
    """Test string with no palindromes."""
    result = find_palindromic_substrings("abc")
    assert set(result) == {"a", "b", "c"}

def test_multiple_palindromes():
    """Test string with multiple palindromes."""
    result = find_palindromic_substrings("racecar")
    expected = {"r", "a", "c", "e", "racecar", "aceca", "cec"}
    assert set(result) == expected

def test_repeated_characters():
    """Test string with repeated characters."""
    result = find_palindromic_substrings("aaa")
    expected = {"a", "aa", "aaa"}
    assert set(result) == expected

def test_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        find_palindromic_substrings(123)
    with pytest.raises(TypeError):
        find_palindromic_substrings(None)