import pytest
from src.subarray_product import count_subarrays_with_product_less_than_k

def test_basic_functionality():
    """Test basic functionality with a simple input"""
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 8

def test_empty_array():
    """Test with an empty array"""
    assert count_subarrays_with_product_less_than_k([], 10) == 0

def test_no_valid_subarrays():
    """Test when no subarrays have product less than k"""
    nums = [10, 20, 30]
    k = 5
    assert count_subarrays_with_product_less_than_k(nums, k) == 0

def test_single_element_array():
    """Test with a single element array"""
    nums = [5]
    k = 10
    assert count_subarrays_with_product_less_than_k(nums, k) == 1

def test_all_elements_less_than_k():
    """Test when all elements are less than k"""
    nums = [1, 2, 3, 4]
    k = 100
    assert count_subarrays_with_product_less_than_k(nums, k) == 10

def test_invalid_k():
    """Test that an invalid k raises a ValueError"""
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k([1, 2, 3], 0)
    
    with pytest.raises(ValueError):
        count_subarrays_with_product_less_than_k([1, 2, 3], -5)

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        count_subarrays_with_product_less_than_k("not a list", 10)
    
    with pytest.raises(TypeError):
        count_subarrays_with_product_less_than_k([1, 2, 3], "not an int")