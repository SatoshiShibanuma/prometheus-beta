import pytest
from src.palindrome_pairs import find_palindrome_pairs, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_basic_palindrome_pairs():
    """Test finding basic palindrome pairs."""
    result = find_palindrome_pairs(["bat", "tab", "cat"])
    assert set(result) == {(0, 1), (1, 0)}

def test_multiple_palindrome_pairs():
    """Test finding multiple palindrome pairs."""
    result = find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    assert set(result) == {(0, 1), (1, 0), (2, 4), (3, 2)}

def test_empty_list():
    """Test behavior with an empty list."""
    result = find_palindrome_pairs([])
    assert result == []

def test_single_element_list():
    """Test behavior with a single-element list."""
    result = find_palindrome_pairs(["abc"])
    assert result == []

def test_input_type_validation():
    """Test input type validation."""
    with pytest.raises(TypeError):
        find_palindrome_pairs("not a list")
    
    with pytest.raises(TypeError):
        find_palindrome_pairs(123)

def test_input_element_validation():
    """Test input element validation."""
    with pytest.raises(ValueError):
        find_palindrome_pairs(["valid", 123, "strings"])

def test_no_palindrome_pairs():
    """Test list with no palindrome pairs."""
    result = find_palindrome_pairs(["abc", "def", "ghi"])
    assert result == []