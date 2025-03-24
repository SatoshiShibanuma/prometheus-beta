import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [1, 2, 3, 4, 5, 10, 100, 7]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases for the perfect number function."""
    # Zero and negative numbers should return False
    assert is_perfect_number(0) == False
    assert is_perfect_number(-6) == False

def test_invalid_input():
    """Test that invalid inputs raise appropriate exceptions."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    with pytest.raises(ValueError):
        is_perfect_number("6")
    with pytest.raises(ValueError):
        is_perfect_number(None)