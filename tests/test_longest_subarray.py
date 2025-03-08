import pytest
from src.longest_subarray import find_longest_subarray

def test_basic_functionality():
    """Test basic scenarios with different input arrays and k values"""
    assert find_longest_subarray([1, 5, 3, 8, 2], 3) == 3
    assert find_longest_subarray([1, 2, 3, 4, 5], 1) == 5
    assert find_longest_subarray([10, 1, 7, 15, 3], 4) == 3

def test_single_element_array():
    """Test array with a single element"""
    assert find_longest_subarray([42], 0) == 1
    assert find_longest_subarray([42], 5) == 1

def test_edge_cases():
    """Test edge cases with different scenarios"""
    # Consecutive elements with large differences
    assert find_longest_subarray([1, 10, 20, 30, 40], 9) == 5
    
    # Alternating elements that just meet the condition
    assert find_longest_subarray([1, 10, 2, 11, 3, 12], 8) == 3

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_longest_subarray([], 5)
    
    with pytest.raises(ValueError, match="k must be a non-negative integer"):
        find_longest_subarray([1, 2, 3], -1)

def test_no_valid_subarray():
    """Test scenarios where no subarray meets the condition"""
    assert find_longest_subarray([1, 2, 3, 4], 5) == 1
    assert find_longest_subarray([10, 11, 12, 13], 10) == 1

def test_large_differences():
    """Test scenarios with large differences"""
    assert find_longest_subarray([1, 100, 200, 300], 50) == 4
    assert find_longest_subarray([1, 1000, 1, 1000], 900) == 2