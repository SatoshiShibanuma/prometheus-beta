import pytest
from src.array_transform import transform_array

def test_transform_array_zeros():
    """Test array with only zeros"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_mixed_numbers():
    """Test array with mixed numbers"""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_transform_array_empty():
    """Test empty array"""
    assert transform_array([]) == []

def test_transform_array_large_numbers():
    """Test with larger numbers"""
    assert transform_array([0, 10, 20]) == [0, 101, 401]

def test_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")

def test_negative_numbers():
    """Test negative numbers raise ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([-1, 2, 3])

def test_non_integer_elements():
    """Test non-integer elements raise ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([1, 2.5, 3])