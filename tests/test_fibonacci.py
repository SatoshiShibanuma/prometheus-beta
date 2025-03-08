import pytest
from src.fibonacci import compute_fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert compute_fibonacci(0) == 0
    assert compute_fibonacci(1) == 1

def test_fibonacci_early_sequence():
    """Test early Fibonacci numbers"""
    assert compute_fibonacci(2) == 1
    assert compute_fibonacci(3) == 2
    assert compute_fibonacci(4) == 3
    assert compute_fibonacci(5) == 5
    assert compute_fibonacci(6) == 8

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers"""
    assert compute_fibonacci(10) == 55
    assert compute_fibonacci(20) == 6765

def test_fibonacci_error_handling():
    """Test error handling for invalid inputs"""
    # Negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        compute_fibonacci(-1)
    
    # Non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        compute_fibonacci("5")

def test_fibonacci_performance():
    """Ensure computation works for relatively large numbers without excessive time/memory"""
    # Large Fibonacci number computation should be quick
    result = compute_fibonacci(100)
    assert result > 0  # 100th Fibonacci number is a large positive integer
    
    # Verify a known large Fibonacci number
    assert compute_fibonacci(50) == 12586269025