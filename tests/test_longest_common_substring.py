import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    """Test basic scenario with a common substring"""
    assert longest_common_substring("programming", "programmer") == "program"

def test_no_common_substring():
    """Test when there's no common substring"""
    assert longest_common_substring("hello", "world") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_substring("test", "test") == "test"

def test_partial_common_substring():
    """Test with partial common substring"""
    assert longest_common_substring("abcdef", "bcdefa") == "bcde"

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("test", "") == ""
    assert longest_common_substring("", "test") == ""

def test_single_character_common():
    """Test with single character common substring"""
    assert longest_common_substring("abc", "cde") == "c"

def test_type_error():
    """Test raising TypeError for non-string inputs"""
    with pytest.raises(TypeError):
        longest_common_substring(123, "test")
    
    with pytest.raises(TypeError):
        longest_common_substring("test", [1, 2, 3])

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_substring("Hello", "hello") == ""

def test_overlapping_substrings():
    """Test with multiple possible overlapping substrings"""
    assert longest_common_substring("ABABC", "BABCA") == "BABC"