import pytest
from src.validate_sequence import is_valid_increasing_sequence

def test_valid_increasing_sequences():
    """Test valid increasing sequences"""
    assert is_valid_increasing_sequence([]) == True
    assert is_valid_increasing_sequence([5]) == True
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([-5, -3, 0, 2, 10]) == True

def test_invalid_increasing_sequences():
    """Test invalid increasing sequences"""
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_increasing_sequence([1, 1, 2, 3, 4]) == False
    assert is_valid_increasing_sequence([1, 2, 2, 3, 4]) == False
    assert is_valid_increasing_sequence([5, 6, 4, 7, 8]) == False

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-list input
    with pytest.raises(TypeError):
        is_valid_increasing_sequence("not a list")
    
    # Test list with non-integer elements
    with pytest.raises(ValueError):
        is_valid_increasing_sequence([1, 2, "3", 4])
    with pytest.raises(ValueError):
        is_valid_increasing_sequence([1, 2, 3.5, 4])
    with pytest.raises(ValueError):
        is_valid_increasing_sequence([1, 2, None, 4])