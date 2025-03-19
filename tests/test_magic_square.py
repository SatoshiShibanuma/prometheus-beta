import pytest
from src.magic_square import is_magic_square

def test_valid_magic_square():
    """Test a classic 3x3 magic square with all unique numbers"""
    # Specific digits representing a valid magic square
    valid_cases = [
        [2, 7, 6, 9, 5, 1, 4, 3, 8],  # 9 numbers
        [2, 7, 6, 9, 5, 1, 4, 3, 8, 10],  # 10 numbers with separator
        [4, 9, 2, 3, 5, 7, 8, 1, 6],  # Another valid configuration
    ]
    for case in valid_cases:
        assert is_magic_square(case) == True, f"Failed for {case}"

def test_invalid_magic_square():
    """Test various invalid magic square configurations"""
    # Incorrect row/column/diagonal sums
    invalid_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],  # No magic square properties
        [1, 2, 3, 4, 5, 6, 7, 8, 10],  # Missing valid grid number
        [1, 1, 1, 1, 1, 1, 1, 1, 1],  # Repeated numbers
    ]
    for case in invalid_cases:
        assert is_magic_square(case) == False, f"Failed for {case}"

def test_incorrect_length():
    """Test lists with incorrect length"""
    assert is_magic_square([1, 2, 3, 4, 5]) == False
    assert is_magic_square([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == False

def test_out_of_range_numbers():
    """Test numbers outside the valid range"""
    assert is_magic_square([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert is_magic_square([10, 11, 12, 13, 14, 15, 16, 17, 18]) == False

def test_input_type():
    """Test non-list inputs"""
    with pytest.raises(ValueError):
        is_magic_square("not a list")
    with pytest.raises(ValueError):
        is_magic_square(12345)

def test_no_separator():
    """Test magic square without separator"""
    assert is_magic_square([4, 9, 2, 3, 5, 7, 8, 1, 6]) == True