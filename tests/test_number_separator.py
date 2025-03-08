import pytest
from src.number_separator import separate_evens_odds

def test_mixed_numbers():
    """Test separating a list with mixed even and odd numbers."""
    result = separate_evens_odds([1, 2, 3, 4, 5, 6])
    assert result == ([2, 4, 6], [1, 3, 5])

def test_empty_list():
    """Test separating an empty list."""
    result = separate_evens_odds([])
    assert result == ([], [])

def test_only_evens():
    """Test a list containing only even numbers."""
    result = separate_evens_odds([2, 4, 6, 8])
    assert result == ([2, 4, 6, 8], [])

def test_only_odds():
    """Test a list containing only odd numbers."""
    result = separate_evens_odds([1, 3, 5, 7])
    assert result == ([], [1, 3, 5, 7])

def test_none_input():
    """Test handling of None input."""
    result = separate_evens_odds(None)
    assert result == ([], [])

def test_negative_numbers():
    """Test handling of negative numbers."""
    result = separate_evens_odds([-1, -2, -3, -4, 0])
    assert result == ([-2, -4, 0], [-1, -3])