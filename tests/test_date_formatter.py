import pytest
from datetime import date
import re
from src.date_formatter import get_current_date_formatted

def test_current_date_format():
    """
    Test that the function returns a date in the correct YYYY-MM-DD format
    """
    # Get the formatted date
    formatted_date = get_current_date_formatted()
    
    # Check that the date is a string
    assert isinstance(formatted_date, str), "Result should be a string"
    
    # Check the format using regex
    # This ensures YYYY-MM-DD pattern with valid date components
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', formatted_date), "Date should be in YYYY-MM-DD format"
    
    # Verify the date matches today's date
    today = date.today().strftime("%Y-%m-%d")
    assert formatted_date == today, "Formatted date should match today's date"

def test_return_type():
    """
    Test the return type of the function
    """
    assert isinstance(get_current_date_formatted(), str), "Function should return a string"