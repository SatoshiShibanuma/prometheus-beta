import pytest
from src.fibonacci_recursive import fibonacci_recursive

def test_fibonacci_first_two_numbers():
    """Test the first two Fibonacci numbers."""
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1

def test_fibonacci_subsequent_numbers():
    """Test subsequent Fibonacci numbers."""
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8
    assert fibonacci_recursive(7) == 13

def test_fibonacci_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_recursive(0)
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        fibonacci_recursive(-1)

def test_fibonacci_invalid_type():
    """Test error handling for non-integer inputs."""
    # Test non-integer input types
    with pytest.raises(TypeError):
        fibonacci_recursive(1.5)
    
    with pytest.raises(TypeError):
        fibonacci_recursive("3")
    
    with pytest.raises(TypeError):
        fibonacci_recursive(None)