import pytest
from src.palindrome_finder import contains_palindrome_word

def test_contains_palindrome_word_simple_palindrome():
    """Test with a simple palindrome word"""
    assert contains_palindrome_word("radar is a cool word") == True

def test_contains_palindrome_word_multiple_words():
    """Test with multiple words including a palindrome"""
    assert contains_palindrome_word("hello world level python") == True

def test_contains_palindrome_word_no_palindrome():
    """Test with no palindrome words"""
    assert contains_palindrome_word("python is awesome") == False

def test_contains_palindrome_word_with_punctuation():
    """Test palindrome with punctuation"""
    assert contains_palindrome_word("wow! what a great day") == True

def test_contains_palindrome_word_mixed_case():
    """Test palindrome with mixed case"""
    assert contains_palindrome_word("Radar is a cool word") == True

def test_contains_palindrome_word_empty_string():
    """Test with empty string"""
    assert contains_palindrome_word("") == False

def test_contains_palindrome_word_special_characters():
    """Test with special characters"""
    assert contains_palindrome_word("hello @racecar@ world") == True

def test_contains_palindrome_word_numbers():
    """Test with numbers"""
    assert contains_palindrome_word("11 is a palindrome number") == True

def test_contains_palindrome_word_short_palindrome():
    """Test with a short palindrome"""
    assert contains_palindrome_word("a") == True

def test_contains_palindrome_word_non_alphabetic():
    """Test with non-alphabetic palindrome"""
    assert contains_palindrome_word("123321 is a number") == True