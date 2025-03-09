import pytest
from src.list_deduplicator import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal while preserving order."""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test handling of empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test list with all identical elements."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_mixed_types():
    """Test that the function works with various integer types."""
    assert remove_duplicates([1, 1, 2, 2, -3, -3, 0]) == [1, 2, -3, 0]

def test_remove_duplicates_large_list():
    """Test performance and correctness with a larger list."""
    large_list = list(range(10)) * 3
    assert remove_duplicates(large_list) == list(range(10))

def test_remove_duplicates_returns_new_list():
    """Ensure the function returns a new list, not modifying the original."""
    original = [1, 2, 3, 2, 4, 1, 5]
    result = remove_duplicates(original)
    assert result != original
    assert result == [1, 2, 3, 4, 5]
    assert original == [1, 2, 3, 2, 4, 1, 5]