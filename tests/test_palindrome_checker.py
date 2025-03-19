import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == False
    assert is_palindrome("a") == True

def test_case_sensitivity():
    """Test case-sensitive palindrome checks"""
    assert is_palindrome("Racecar") == False
    assert is_palindrome("RaceCar") == False

def test_numbers_and_special_chars():
    """Test palindromes with numbers and special characters"""
    assert is_palindrome("12321") == True
    assert is_palindrome("!@#$%^&*") == False
    assert is_palindrome("a1b2c2b1a") == True
    assert is_palindrome("a1b2c3b1a") == False

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("openai") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome(None) == False
    assert is_palindrome("") == False