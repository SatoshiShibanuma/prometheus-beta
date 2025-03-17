import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_numbers():
    """Test sum_digits with various positive integers."""
    assert sum_digits(123) == 6
    assert sum_digits(9876) == 30
    assert sum_digits(1000) == 1
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test sum_digits with single-digit numbers."""
    for i in range(10):
        assert sum_digits(i) == i

def test_sum_digits_invalid_inputs():
    """Test sum_digits with invalid input types and values."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_digits(-123)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_digits(None)