import pytest
from src.lcs import longest_common_subsequence

def test_lcs_basic_cases():
    """Test basic longest common subsequence scenarios."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_empty_strings():
    """Test scenarios with empty strings."""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_lcs_identical_strings():
    """Test when strings are identical."""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_no_common_substring():
    """Test when there's no common subsequence."""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_case_sensitive():
    """Test case sensitivity."""
    # Strictly case-sensitive matching
    assert longest_common_subsequence("AbC", "aBC") == ""  # Different cases
    assert longest_common_subsequence("ABCDE", "ABCDE") == "ABCDE"  # Exact match
    assert longest_common_subsequence("AbCdE", "AbCdE") == "AbCdE"  # Exact case match

def test_lcs_long_strings():
    """Test with longer input strings."""
    s1 = "ABCBDAB" * 10
    s2 = "BDCABA" * 10
    result = longest_common_subsequence(s1, s2)
    assert len(result) > 0

def test_lcs_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", ['a', 'b', 'c'])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, None)