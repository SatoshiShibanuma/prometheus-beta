import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_range():
    """Test a basic range where some numbers are multiples of 2 or 3"""
    assert sum_of_multiples(1, 10) == 42  # 2+3+4+6+8+9+10

def test_range_with_no_multiples():
    """Test a range with no multiples of 2 or 3"""
    assert sum_of_multiples(7, 7) == 0

def test_single_multiple():
    """Test a range with a single multiple"""
    assert sum_of_multiples(6, 6) == 6

def test_larger_range():
    """Test a larger range"""
    assert sum_of_multiples(1, 20) == 137

def test_equal_min_max():
    """Test when min and max are equal and a multiple"""
    assert sum_of_multiples(6, 6) == 6

def test_equal_min_max_not_multiple():
    """Test when min and max are equal and not a multiple"""
    assert sum_of_multiples(5, 5) == 0

def test_invalid_range():
    """Test that an error is raised when min > max"""
    with pytest.raises(ValueError, match="Minimum value must be less than or equal to maximum value"):
        sum_of_multiples(10, 5)

def test_zero_range():
    """Test a range starting from zero"""
    assert sum_of_multiples(0, 5) == 9  # 0 + 3 + 6