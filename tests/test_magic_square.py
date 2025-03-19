import pytest
from src.magic_square import is_magic_square

def test_valid_magic_square():
    """Test a classic 3x3 magic square with all unique numbers"""
    assert is_magic_square([2, 7, 6, 9, 5, 1, 4, 3, 8, 10]) == True
    assert is_magic_square([4, 9, 2, 3, 5, 7, 8, 1, 6, 10]) == True

def test_invalid_magic_square():
    """Test various invalid magic square configurations"""
    # Incorrect row/column/diagonal sums
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    
    # Missing numbers
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 10]) == False
    
    # Repeated numbers
    assert is_magic_square([1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == False

def test_incorrect_length():
    """Test lists with incorrect length"""
    assert is_magic_square([1, 2, 3, 4, 5]) == False
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False

def test_out_of_range_numbers():
    """Test numbers outside the valid range"""
    assert is_magic_square([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]) == False
    assert is_magic_square([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == False

def test_input_type():
    """Test non-list inputs"""
    with pytest.raises(ValueError):
        is_magic_square("not a list")
    with pytest.raises(ValueError):
        is_magic_square(12345)

def test_no_separator():
    """Test magic square without separator"""
    assert is_magic_square([2, 7, 6, 9, 5, 1, 4, 3, 8]) == True