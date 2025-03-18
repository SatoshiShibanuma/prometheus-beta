import pytest
from src.simple_calculator import simple_calculator

def test_addition():
    """Test addition operation"""
    assert simple_calculator(2, 3, '+') == 5
    assert simple_calculator(-1, 1, '+') == 0
    assert simple_calculator(0, 0, '+') == 0

def test_subtraction():
    """Test subtraction operation"""
    assert simple_calculator(5, 3, '-') == 2
    assert simple_calculator(-1, 1, '-') == -2
    assert simple_calculator(0, 0, '-') == 0

def test_multiplication():
    """Test multiplication operation"""
    assert simple_calculator(2, 3, '*') == 6
    assert simple_calculator(-1, 1, '*') == -1
    assert simple_calculator(0, 5, '*') == 0

def test_division():
    """Test division operation"""
    assert simple_calculator(6, 3, '/') == 2
    assert simple_calculator(-6, 3, '/') == -2
    assert simple_calculator(0, 5, '/') == 0

def test_division_by_zero():
    """Test division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        simple_calculator(5, 0, '/')

def test_invalid_operator():
    """Test invalid operator raises ValueError"""
    with pytest.raises(ValueError):
        simple_calculator(5, 3, '%')
    with pytest.raises(ValueError):
        simple_calculator(5, 3, '')
    with pytest.raises(ValueError):
        simple_calculator(5, 3, None)

def test_whitespace_handling():
    """Test operator works with whitespace"""
    assert simple_calculator(2, 3, ' + ') == 5
    assert simple_calculator(6, 3, ' / ') == 2