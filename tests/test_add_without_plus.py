import pytest
from src.add_without_plus import add_without_plus

def test_add_positive_numbers():
    """Test addition of positive numbers"""
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5

def test_add_negative_numbers():
    """Test addition of negative numbers"""
    assert add_without_plus(-3, -4) == -7
    assert add_without_plus(-10, -20) == -30
    assert add_without_plus(-5, 5) == 0

def test_add_large_numbers():
    """Test addition of larger numbers"""
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 1000) == 0

def test_input_validation():
    """Test input type validation"""
    with pytest.raises(TypeError):
        add_without_plus(3.5, 4)
    with pytest.raises(TypeError):
        add_without_plus("3", 4)
    with pytest.raises(TypeError):
        add_without_plus(None, 4)

def test_zero_addition():
    """Test addition with zero"""
    assert add_without_plus(0, 0) == 0