import pytest
from src.remove_duplicates import remove_duplicates_and_sort

def test_remove_duplicates_and_sort_basic():
    """Test basic functionality of removing duplicates and sorting"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert remove_duplicates_and_sort(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    assert remove_duplicates_and_sort([]) == []

def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort(input_list) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test with a list of all duplicate elements"""
    input_list = [2, 2, 2, 2, 2]
    assert remove_duplicates_and_sort(input_list) == [2]

def test_remove_duplicates_negative_numbers():
    """Test with negative numbers"""
    input_list = [-3, 1, -3, 4, 1, -1, 4]
    expected = [-3, -1, 1, 4]
    assert remove_duplicates_and_sort(input_list) == expected

def test_invalid_input_non_list():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates_and_sort("not a list")

def test_invalid_input_non_integers():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_duplicates_and_sort([1, 2, "3", 4])