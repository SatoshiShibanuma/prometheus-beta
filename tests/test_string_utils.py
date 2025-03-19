import pytest
from src.string_utils import reverse_substring

def test_reverse_substring_basic():
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_reverse_substring_full_string():
    assert reverse_substring("python", 0, 6) == "nohtyp"

def test_reverse_substring_partial():
    assert reverse_substring("programming", 2, 7) == "pramgroming"

def test_reverse_substring_same_indices():
    assert reverse_substring("test", 2, 2) == "test"

def test_reverse_substring_error_handling():
    # Test type errors
    with pytest.raises(TypeError):
        reverse_substring(123, 0, 3)
    
    # Test index out of bounds
    with pytest.raises(ValueError):
        reverse_substring("test", -1, 4)
    with pytest.raises(ValueError):
        reverse_substring("test", 0, 5)
    
    # Test invalid index range
    with pytest.raises(ValueError):
        reverse_substring("test", 3, 2)

def test_reverse_substring_edge_cases():
    assert reverse_substring("a", 0, 1) == "a"
    assert reverse_substring("", 0, 0) == ""