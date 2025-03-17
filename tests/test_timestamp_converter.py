import pytest
from datetime import datetime
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from timestamp_converter import convert_timestamp_to_readable_date

def test_valid_timestamp():
    """Test conversion of a known timestamp"""
    # Using a specific timestamp (e.g., January 1, 2020 at midnight UTC)
    timestamp = 1577836800
    assert convert_timestamp_to_readable_date(timestamp) == "January 01, 2020"

def test_float_timestamp():
    """Test conversion with a float timestamp"""
    timestamp = 1577836800.123
    assert convert_timestamp_to_readable_date(timestamp) == "January 01, 2020"

def test_current_timestamp():
    """Test conversion with current timestamp"""
    current_timestamp = datetime.now().timestamp()
    readable_date = convert_timestamp_to_readable_date(current_timestamp)
    assert isinstance(readable_date, str)
    assert len(readable_date) > 0

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        convert_timestamp_to_readable_date("not a number")
    
    with pytest.raises(TypeError):
        convert_timestamp_to_readable_date(None)
    
    with pytest.raises(TypeError):
        convert_timestamp_to_readable_date([1, 2, 3])

def test_negative_timestamp():
    """Test error handling for negative timestamp"""
    with pytest.raises(ValueError):
        convert_timestamp_to_readable_date(-1000)

def test_zero_timestamp():
    """Test conversion of zero timestamp"""
    assert convert_timestamp_to_readable_date(0) == "January 01, 1970"