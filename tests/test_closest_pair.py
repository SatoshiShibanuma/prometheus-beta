import pytest
from src.closest_pair import find_closest_pair

def test_basic_case():
    """Test a basic scenario with different numbers."""
    assert find_closest_pair([1, 3, 4, 10]) == (3, 4)

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_closest_pair([-1, -3, 5, 10, 20]) == (-3, -1)

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert find_closest_pair([-5, 2, 3, 10, 15]) == (2, 3)

def test_multiple_pairs_with_same_diff():
    """Test when multiple pairs have the same difference."""
    # 1 and 2 have the same difference as 3 and 4, 
    # but 1 and 2 should be returned as they are smaller
    assert find_closest_pair([1, 2, 3, 4, 10]) == (1, 2)

def test_duplicate_numbers():
    """Test with duplicate numbers."""
    assert find_closest_pair([5, 5, 5, 5]) == (5, 5)

def test_two_numbers():
    """Test with exactly two numbers."""
    assert find_closest_pair([100, 200]) == (100, 200)

def test_error_empty_list():
    """Test that an error is raised for an empty list."""
    with pytest.raises(ValueError):
        find_closest_pair([])

def test_error_single_number():
    """Test that an error is raised for a list with only one number."""
    with pytest.raises(ValueError):
        find_closest_pair([42])

def test_large_list():
    """Test with a larger list of numbers."""
    assert find_closest_pair([1, 5, 10, 20, 30, 40, 50]) == (1, 5)

def test_floating_point_numbers():
    """Test with floating point numbers."""
    assert find_closest_pair([1.1, 1.2, 5.5, 10.0]) == (1.1, 1.2)