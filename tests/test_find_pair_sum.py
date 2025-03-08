import pytest
from src.find_pair_sum import find_pairs_with_target_sum

def test_basic_pair_sum():
    """Test finding pairs that sum to a target in a simple list"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_pairs_with_target_sum(arr, target)) == sorted(expected)

def test_empty_list():
    """Test behavior with an empty list"""
    arr = []
    target = 5
    assert find_pairs_with_target_sum(arr, target) == []

def test_no_pairs_found():
    """Test when no pairs sum to the target"""
    arr = [1, 2, 3, 4, 5]
    target = 100
    assert find_pairs_with_target_sum(arr, target) == []

def test_single_element_list():
    """Test with a single element list"""
    arr = [5]
    target = 10
    assert find_pairs_with_target_sum(arr, target) == []

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pairs_with_target_sum("not a list", 10)
    
    with pytest.raises(TypeError, match="Target sum must be an integer"):
        find_pairs_with_target_sum([1, 2, 3], "not an int")

def test_duplicate_elements():
    """Test that duplicate elements are not allowed"""
    with pytest.raises(ValueError, match="Input array must contain unique elements"):
        find_pairs_with_target_sum([1, 2, 2, 3], 5)

def test_large_array():
    """Test with a larger array"""
    arr = list(range(1, 21))  # 1 to 20
    target = 30
    expected = [(10, 20), (11, 19), (12, 18), (13, 17), (14, 16)]
    assert sorted(find_pairs_with_target_sum(arr, target)) == sorted(expected)

def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-3, -2, -1, 0, 1, 2, 3]
    target = 0
    expected = [(-3, 3), (-2, 2), (-1, 1)]
    assert sorted(find_pairs_with_target_sum(arr, target)) == sorted(expected)