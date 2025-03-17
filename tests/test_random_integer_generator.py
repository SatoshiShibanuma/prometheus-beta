import pytest
import src.random_integer_generator as rig

def test_generate_random_integer_within_range():
    """Test that the generated integer is within the specified range."""
    min_val, max_val = 1, 10
    result = rig.generate_random_integer(min_val, max_val)
    
    assert isinstance(result, int), "Result should be an integer"
    assert min_val <= result <= max_val, f"Result {result} should be between {min_val} and {max_val}"

def test_generate_random_integer_single_number():
    """Test generating a random integer when min and max are the same."""
    result = rig.generate_random_integer(5, 5)
    assert result == 5, "Result should be the same as min and max"

def test_generate_random_integer_negative_range():
    """Test generating a random integer in a negative range."""
    min_val, max_val = -10, -1
    result = rig.generate_random_integer(min_val, max_val)
    
    assert isinstance(result, int), "Result should be an integer"
    assert min_val <= result <= max_val, f"Result {result} should be between {min_val} and {max_val}"

def test_generate_random_integer_invalid_range():
    """Test that an error is raised when min_value is greater than max_value."""
    with pytest.raises(ValueError, match="min_value must be less than or equal to max_value"):
        rig.generate_random_integer(10, 5)

def test_generate_random_integer_invalid_type():
    """Test that an error is raised when input is not an integer."""
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        rig.generate_random_integer(1.5, 5)
    
    with pytest.raises(TypeError, match="Both min_value and max_value must be integers"):
        rig.generate_random_integer(1, "5")

def test_random_distribution():
    """Test that the function produces varied results over multiple calls."""
    results = set()
    for _ in range(100):
        results.add(rig.generate_random_integer(1, 10))
    
    # If the function works correctly, we should get multiple different values
    assert len(results) > 1, "Should generate varied random numbers"