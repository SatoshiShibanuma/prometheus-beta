import pytest
from src.string_converter import convert_to_alternating_snake_case

def test_basic_conversion():
    """Test basic conversion of simple strings"""
    assert convert_to_alternating_snake_case("Hello World") == 'hello_World'
    assert convert_to_alternating_snake_case("PYTHON PROGRAMMING") == 'python_PROGRAMMING'

def test_multiple_words():
    """Test conversion with multiple words"""
    assert convert_to_alternating_snake_case("The Quick Brown Fox") == 'the_Quick_brown_Fox'

def test_empty_string():
    """Test conversion of empty string"""
    assert convert_to_alternating_snake_case("") == ""

def test_single_word():
    """Test conversion of a single word"""
    assert convert_to_alternating_snake_case("Hello") == 'hello'

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_snake_case(None)

def test_edge_cases():
    """Test various edge cases"""
    assert convert_to_alternating_snake_case(" ") == ""
    assert convert_to_alternating_snake_case("a b c d") == 'a_B_c_D'
    assert convert_to_alternating_snake_case("HELLO world PYTHON program") == 'hello_World_python_Program'