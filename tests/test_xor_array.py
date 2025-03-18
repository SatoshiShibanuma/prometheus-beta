import pytest
from src.xor_array import xor_array_elements

def test_xor_array_basic():
    """Test XOR of a basic array of integers."""
    assert xor_array_elements([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0

def test_xor_array_single_element():
    """Test XOR with a single element returns that element."""
    assert xor_array_elements([42]) == 42

def test_xor_array_multiple_elements():
    """Test XOR with multiple elements."""
    assert xor_array_elements([5, 3, 7]) == 1  # 5 ^ 3 ^ 7 = 1

def test_xor_array_zero_elements():
    """Test XOR with zero elements raises ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        xor_array_elements([])

def test_xor_array_non_list_input():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        xor_array_elements(42)

def test_xor_array_non_integer_elements():
    """Test that list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        xor_array_elements([1, 2, "3"])

def test_xor_array_large_numbers():
    """Test XOR with larger numbers."""
    assert xor_array_elements([1000, 2000, 3000]) == 0  # 1000 ^ 2000 ^ 3000 = 0

def test_xor_array_negative_numbers():
    """Test XOR with negative numbers."""
    assert xor_array_elements([-1, -2, -3]) == 0  # -1 ^ -2 ^ -3 = 0