import pytest
from src.list_sum import find_smallest_list_sum

def test_basic_smallest_sum():
    """Test basic scenario with positive numbers"""
    assert find_smallest_list_sum([1, 2, 3], [4, 5, 6]) == 5

def test_negative_numbers():
    """Test with lists containing negative numbers"""
    assert find_smallest_list_sum([-1, -2], [-3, -4]) == -6

def test_mixed_numbers():
    """Test with mixed positive and negative numbers"""
    assert find_smallest_list_sum([-1, 1], [2, -2]) == -3

def test_single_element_lists():
    """Test with single-element lists"""
    assert find_smallest_list_sum([5], [3]) == 8

def test_large_numbers():
    """Test with large numbers"""
    assert find_smallest_list_sum([1000], [2000]) == 3000

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError"""
    with pytest.raises(ValueError, match="Lists cannot be empty"):
        find_smallest_list_sum([], [1, 2, 3])
    with pytest.raises(ValueError, match="Lists cannot be empty"):
        find_smallest_list_sum([1, 2, 3], [])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_list_sum(1, [2, 3])
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_list_sum([1, 2], "3")

def test_non_integer_input_raises_error():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All list elements must be integers"):
        find_smallest_list_sum([1, 'a'], [2, 3])
    with pytest.raises(ValueError, match="All list elements must be integers"):
        find_smallest_list_sum([1, 2], [3, 4.5])