import pytest
from src.palindrome import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_complex_palindromes():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_insensitivity():
    """Test case-insensitive palindrome checking."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert is_palindrome(" ") == True  # Space-only input
    assert is_palindrome("!@#$%^&*()") == True  # Only punctuation
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("ab") == False  # Two different characters
    assert is_palindrome("") == True  # Empty string