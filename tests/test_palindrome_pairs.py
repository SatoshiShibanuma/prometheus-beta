import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert sorted(result) == [[0, 1], [1, 0]]

def test_empty_list():
    """Test an empty input list."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word_list():
    """Test a list with only one word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected = [[0, 1], [1, 0], [3, 4], [4, 3]]
    assert sorted(result) == sorted(expected)

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["cat", "dog", "bird"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_same_word_repeated():
    """Test scenario with the same word repeated."""
    words = ["a", "a"]
    result = find_palindrome_pairs(words)
    assert sorted(result) == [[0, 1], [1, 0]]

def test_edge_case_different_word_lengths():
    """Test palindrome pairs with words of different lengths."""
    words = ["abc", "cba", "x", "y", "xyyx"]
    result = find_palindrome_pairs(words)
    expected = [[0, 1], [1, 0], [3, 4], [4, 3]]
    assert sorted(result) == sorted(expected)