import pytest
from src.even_sum_odd_count import analyze_numbers

def test_mixed_numbers():
    """Test a list with mixed even and odd numbers."""
    result = analyze_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_empty_list():
    """Test an empty list returns (0, 0)."""
    result = analyze_numbers([])
    assert result == (0, 0)

def test_only_even_numbers():
    """Test a list with only even numbers."""
    result = analyze_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_only_odd_numbers():
    """Test a list with only odd numbers."""
    result = analyze_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_negative_numbers():
    """Test a list with negative numbers."""
    result = analyze_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-12, 3)

def test_invalid_input_non_list():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_numbers("not a list")

def test_invalid_input_non_integers():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        analyze_numbers([1, 2, "3", 4])