import pytest
from src.max_subarray_sum import max_subarray_sum_with_constraints

def test_basic_valid_subarray():
    """Test a basic case with a valid subarray"""
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 2, 10) == 12

def test_multiple_valid_subarrays():
    """Test when multiple subarrays meet the constraints"""
    A = [1, 2, 3, 4, 5, 6]
    assert max_subarray_sum_with_constraints(A, 3, 15) == 15

def test_no_valid_subarray():
    """Test when no subarray meets the constraints"""
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 3, 100) is None

def test_minimum_length_constraint():
    """Test the minimum length constraint"""
    A = [1, 2, 3, 4, 5]
    assert max_subarray_sum_with_constraints(A, 5, 10) == 15

def test_negative_numbers():
    """Test with negative numbers"""
    A = [-1, -2, 3, 4, -5, 6, 7]
    assert max_subarray_sum_with_constraints(A, 3, 10) == 17

def test_all_negative_numbers():
    """Test when all numbers are negative"""
    A = [-1, -2, -3, -4, -5]
    assert max_subarray_sum_with_constraints(A, 2, -10) is None

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints("not a list", 2, 10)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], "not an int", 10)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], 2, "not an int")

def test_invalid_k_value():
    """Test error handling for invalid k value"""
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], 0, 10)
    
    with pytest.raises(ValueError):
        max_subarray_sum_with_constraints([1, 2, 3], -1, 10)

def test_empty_array():
    """Test with an empty array"""
    assert max_subarray_sum_with_constraints([], 2, 10) is None

def test_array_shorter_than_k():
    """Test when array is shorter than k"""
    A = [1, 2]
    assert max_subarray_sum_with_constraints(A, 3, 10) is None