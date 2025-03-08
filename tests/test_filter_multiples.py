import pytest
from src.filter_multiples import filter_special_multiples

def test_basic_filtering():
    """Test basic functionality of filtering multiples"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
    expected = [3, 5, 6, 9, 10]
    assert filter_special_multiples(input_list) == expected

def test_empty_list():
    """Test filtering an empty list"""
    assert filter_special_multiples([]) == []

def test_no_special_multiples():
    """Test list with no special multiples"""
    input_list = [1, 2, 4, 7, 11, 13]
    assert filter_special_multiples(input_list) == []

def test_only_special_multiples():
    """Test list with only special multiples"""
    input_list = [3, 5, 6, 9, 10, 15]
    expected = [3, 5, 6, 9, 10]
    assert filter_special_multiples(input_list) == expected

def test_negative_numbers():
    """Test filtering with negative numbers"""
    input_list = [-3, -5, -6, -9, -10, -15, 0, 3, 5, 6, 9, 10]
    expected = [-3, 3, -5, 5, -6, 6, -9, 9, -10, 10]
    assert filter_special_multiples(input_list) == expected

def test_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_special_multiples("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_special_multiples(123)

def test_non_integer_elements():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        filter_special_multiples([1, 2, "3", 4])
    with pytest.raises(ValueError, match="All elements must be integers"):
        filter_special_multiples([1, 2, 3.5, 4])