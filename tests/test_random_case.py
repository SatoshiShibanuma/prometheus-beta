import pytest
import random
from src.random_case import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Check that the result is the same length as input
    assert len(result) == len(input_str)
    
    # Ensure some characters are different case
    assert result.lower() != result and result.upper() != result

def test_convert_to_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_type_error():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test the randomness of the conversion."""
    # Set a fixed random seed for reproducibility
    random.seed(42)
    
    input_str = "abcdefg"
    results = set()
    
    # Generate multiple conversions to check randomness
    for _ in range(10):
        result = convert_to_random_case(input_str)
        results.add(result)
        
        # Verify result meets requirements
        assert len(result) == len(input_str)
    
    # Ensure we get different results across multiple calls (with more tolerance)
    assert len(results) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and mixed case."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Check that the result preserves non-alphabetic characters
    assert result != input_str
    assert len(result) == len(input_str)
    
    # Check that digits and punctuation remain unchanged
    import re
    assert re.sub(r'[a-zA-Z]', '', result) == re.sub(r'[a-zA-Z]', '', input_str)