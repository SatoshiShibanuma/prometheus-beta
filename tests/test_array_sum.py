import pytest
from src.array_sum import sum_odd_even_numbers

def test_mixed_numbers():
    """Test with a mix of odd and even numbers."""
    result = sum_odd_even_numbers([1, 2, 3, 4, 5])
    assert result == (9, 6)

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = sum_odd_even_numbers([1, 3, 5, 7])
    assert result == (16, 0)

def test_only_even_numbers():
    """Test with only even numbers."""
    result = sum_odd_even_numbers([2, 4, 6, 8])
    assert result == (0, 20)

def test_empty_list():
    """Test with an empty list."""
    result = sum_odd_even_numbers([])
    assert result == (0, 0)

def test_negative_numbers():
    """Test with negative numbers."""
    result = sum_odd_even_numbers([-1, -2, -3, -4, -5])
    assert result == (-9, -6)

def test_mixed_negative_positive():
    """Test with mixed negative and positive numbers."""
    result = sum_odd_even_numbers([-1, 2, -3, 4, 5])
    assert result == (1, 6)

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_odd_even_numbers(123)

def test_invalid_input_non_integers():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_odd_even_numbers([1, 2, 'three', 4])