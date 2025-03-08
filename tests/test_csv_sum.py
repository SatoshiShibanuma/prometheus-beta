import pytest
from src.csv_sum import parse_csv_sum

def test_parse_csv_sum_basic():
    """Test parsing and summing a simple CSV of numbers."""
    assert parse_csv_sum("1,2,3") == 6

def test_parse_csv_sum_with_spaces():
    """Test parsing CSV with whitespace around numbers."""
    assert parse_csv_sum(" 1 , 2 , 3 ") == 6

def test_parse_csv_sum_single_number():
    """Test parsing a single number."""
    assert parse_csv_sum("42") == 42

def test_parse_csv_sum_empty_string():
    """Test handling of empty string."""
    assert parse_csv_sum("") == 0

def test_parse_csv_sum_negative_numbers():
    """Test parsing CSV with negative numbers."""
    assert parse_csv_sum("-1,2,-3") == -2

def test_parse_csv_sum_invalid_input():
    """Test raising ValueError for non-integer input."""
    with pytest.raises(ValueError, match="Input must contain only integers separated by commas"):
        parse_csv_sum("1,2,three")

def test_parse_csv_sum_mixed_invalid_input():
    """Test raising ValueError for mixed valid and invalid input."""
    with pytest.raises(ValueError, match="Input must contain only integers separated by commas"):
        parse_csv_sum("1,2,3.5")