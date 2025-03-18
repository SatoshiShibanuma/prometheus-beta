import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_early_sequence():
    """Test early Fibonacci numbers"""
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers"""
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_memoization():
    """Verify that memoization works by creating a memo dictionary"""
    memo = {}
    result1 = fibonacci(20, memo)
    result2 = fibonacci(20, memo)
    
    # Ensure the same result is returned
    assert result1 == result2
    
    # Verify the value is correct
    assert result1 == 6765