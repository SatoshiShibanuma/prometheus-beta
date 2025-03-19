import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_arr = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert deleteDuplicates(input_arr) == expected

def test_delete_duplicates_empty_list():
    """Test handling of an empty list"""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_all_same():
    """Test list with all identical elements"""
    assert deleteDuplicates([1, 1, 1, 1]) == [1]

def test_delete_duplicates_order_preservation():
    """Test that the first occurrence order is maintained"""
    input_arr = [5, 2, 3, 2, 5, 1, 3]
    expected = [5, 2, 3, 1]
    assert deleteDuplicates(input_arr) == expected

def test_delete_duplicates_mixed_types():
    """Test with mixed but similar elements"""
    input_arr = [1, 1.0, 2, 2.0, 3]
    expected = [1, 2, 3]
    assert deleteDuplicates(input_arr) == expected

def test_delete_duplicates_negative_nums():
    """Test with negative numbers"""
    input_arr = [-1, -1, 0, 1, 1, -1]
    expected = [-1, 0, 1]
    assert deleteDuplicates(input_arr) == expected