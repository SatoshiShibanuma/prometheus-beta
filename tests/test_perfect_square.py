import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test non-perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 12, 15, 17, 20]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_float_perfect_squares():
    """Test perfect squares with floating point precision."""
    assert is_perfect_square(4.0) is True
    assert is_perfect_square(9.0) is True
    assert is_perfect_square(16.0) is True

def test_float_non_perfect_squares():
    """Test non-perfect squares with floating point precision."""
    assert is_perfect_square(4.1) is False
    assert is_perfect_square(8.99) is False

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    
    # Test invalid input types
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)

def test_large_perfect_squares():
    """Test large perfect squares."""
    large_perfect_squares = [10000, 1000000, 10**6]
    for num in large_perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"