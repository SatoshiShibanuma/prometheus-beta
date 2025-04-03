import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_case():
    """Test a basic scenario with positive integers"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39

def test_all_positive():
    """Test an array with all positive numbers"""
    arr = [100, 200, 300, 400, 500]
    k = 3
    assert max_subarray_sum(arr, k) == 1200

def test_mixed_numbers():
    """Test an array with mixed positive and negative numbers"""
    arr = [-1, 4, -2, 10, -5, 3, 2, 0]
    k = 3
    assert max_subarray_sum(arr, k) == 12

def test_all_negative():
    """Test an array with all negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3

def test_empty_array_with_zero_k():
    """Test an empty array with k=0"""
    arr = []
    k = 0
    assert max_subarray_sum(arr, k) == 0

def test_empty_array_with_non_zero_k():
    """Test an empty array with non-zero k"""
    arr = []
    with pytest.raises(ValueError, match="Cannot compute subarray sum for an empty array"):
        max_subarray_sum(arr, 1)

def test_k_equals_array_length():
    """Test when k is equal to array length"""
    arr = [1, 2, 3, 4, 5]
    k = 5
    assert max_subarray_sum(arr, k) == 15

def test_k_is_one():
    """Test when k is 1"""
    arr = [5, 2, 7, 1, 9, 3]
    k = 1
    assert max_subarray_sum(arr, k) == 9

def test_invalid_k_too_small():
    """Test when k is less than 1"""
    with pytest.raises(ValueError, match="Subarray length must be at least 1"):
        max_subarray_sum([1, 2, 3], 0)

def test_invalid_k_too_large():
    """Test when k is larger than array length"""
    with pytest.raises(ValueError, match="Subarray length cannot be larger than array length"):
        max_subarray_sum([1, 2, 3], 4)

def test_invalid_input_type():
    """Test when input is not a list"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list", 2)

def test_invalid_k_type():
    """Test when k is not an integer"""
    with pytest.raises(TypeError, match="Subarray length must be an integer"):
        max_subarray_sum([1, 2, 3], "2")