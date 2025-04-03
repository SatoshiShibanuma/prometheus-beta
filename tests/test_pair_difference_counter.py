import pytest
from src.pair_difference_counter import count_pairs_with_difference_of_five

def test_basic_pairs():
    """Test basic scenario with pairs having a difference of 5"""
    assert count_pairs_with_difference_of_five([1, 6, 3, 8, 4, 9]) == 3

def test_empty_list():
    """Test an empty list returns 0"""
    assert count_pairs_with_difference_of_five([]) == 0

def test_single_element_list():
    """Test a list with only one element returns 0"""
    assert count_pairs_with_difference_of_five([5]) == 0

def test_no_matching_pairs():
    """Test a list with no pairs having a difference of 5"""
    assert count_pairs_with_difference_of_five([1, 2, 3, 4, 5]) == 0

def test_negative_numbers():
    """Test pairs with negative numbers"""
    assert count_pairs_with_difference_of_five([-1, 4, 0, 5, 10, 5]) == 4

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_pairs_with_difference_of_five(123)

def test_invalid_list_content():
    """Test that ValueError is raised for non-integer list elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        count_pairs_with_difference_of_five([1, 2, 'a', 4])

def test_absolute_difference():
    """Test that the difference works in both directions"""
    assert count_pairs_with_difference_of_five([6, 1, 9, 4, 14, 9]) == 3