import pytest
from src.triangle_number import triangle_number

def test_triangle_numbers():
    """Test known Triangle Numbers."""
    triangle_nums = [6, 28, 10, 15, 21]
    for num in triangle_nums:
        assert triangle_number(num) == True, f"{num} should be a Triangle Number"

def test_non_triangle_numbers():
    """Test numbers that are not Triangle Numbers."""
    non_triangle_nums = [7, 12, 16, 25, 30]
    for num in non_triangle_nums:
        assert triangle_number(num) == False, f"{num} should not be a Triangle Number"

def test_single_digit_triangle_numbers():
    """Test single-digit Triangle Numbers."""
    assert triangle_number(1) == True
    assert triangle_number(3) == True

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        triangle_number(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        triangle_number(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        triangle_number(3.14)

def test_large_triangle_number():
    """Test a larger Triangle Number."""
    assert triangle_number(496) == True  # 496 is indeed a Triangle Number