import pytest
from src.unique_chars_sorter import sort_unique_chars

def test_basic_string():
    """Test sorting unique characters in a basic string."""
    assert sort_unique_chars("hello") == ['e', 'h', 'l', 'o']

def test_case_sensitivity():
    """Test that the sorting is case-sensitive."""
    assert sort_unique_chars("Python") == ['P', 'h', 'n', 'o', 't', 'y']

def test_empty_string():
    """Test handling of an empty string."""
    assert sort_unique_chars("") == []

def test_string_with_spaces():
    """Test string with spaces and mixed characters."""
    assert sort_unique_chars("a b C") == [' ', 'C', 'a', 'b']

def test_repeated_characters():
    """Test string with repeated characters."""
    assert sort_unique_chars("banana") == ['a', 'b', 'n']

def test_special_characters():
    """Test string with special characters."""
    assert sort_unique_chars("Hello, World!") == [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r']