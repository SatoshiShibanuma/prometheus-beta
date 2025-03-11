import pytest
from src.counting_sort import counting_sort

def test_normal_sorting():
    """Test sorting a list of non-negative integers."""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list."""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element."""
    assert counting_sort([42]) == [42]

def test_already_sorted():
    """Test sorting a list that is already sorted."""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_all_same_elements():
    """Test sorting a list with all elements being the same."""
    assert counting_sort([3, 3, 3, 3]) == [3, 3, 3, 3]

def test_large_numbers():
    """Test sorting a list with larger numbers."""
    assert counting_sort([100, 2, 56, 200, 1]) == [1, 2, 56, 100, 200]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, -2, 3])