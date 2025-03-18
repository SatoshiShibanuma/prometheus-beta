import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test counting palindromes in an empty string."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test that each single character is a palindrome."""
    assert count_palindromic_substrings("a") == 1

def test_simple_palindromes():
    """Test basic palindrome scenarios."""
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6

def test_mixed_palindromes():
    """Test strings with multiple palindromic substrings."""
    assert count_palindromic_substrings("racecar") == 10

def test_with_punctuation():
    """Test palindrome counting with punctuation and spaces."""
    assert count_palindromic_substrings("A man, a plan, a canal: Panama") == 27

def test_case_insensitive():
    """Ensure palindrome detection is case-insensitive."""
    assert count_palindromic_substrings("Aba") == 4

def test_complex_palindromes():
    """Test more complex palindrome scenarios."""
    assert count_palindromic_substrings("hello") == 5
    assert count_palindromic_substrings("abcba") == 7