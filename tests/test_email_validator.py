import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email addresses."""
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "user123@example-domain.com",
        "first.last@example.org",
        "user+tag@example.net"
    ]
    for email in valid_emails:
        assert validate_email(email) is True, f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email addresses."""
    invalid_emails = [
        "",  # Empty string
        "invalid-email",  # No @ symbol
        "@example.com",  # No local part
        "user@",  # No domain
        "user@.com",  # Invalid domain
        "user@example",  # Missing top-level domain
        "user@example..com",  # Double dot in domain
        123,  # Non-string input
        "a" * 255 + "@example.com"  # Too long
    ]
    for email in invalid_emails:
        assert validate_email(email) is False, f"{email} should be invalid"

def test_edge_cases():
    """Test edge case email formats."""
    edge_cases = [
        "a@b.co",  # Minimum possible valid email
        "user@example.museum",  # Longer TLD
        "user+tag+another@example.com"  # Multiple + tags
    ]
    for email in edge_cases:
        assert validate_email(email) is True, f"{email} should be valid"

def test_special_characters():
    """Test email addresses with special characters."""
    special_char_emails = [
        "first.last@example.com",
        "user.name+tag@example.org",
        "user_name@example.net"
    ]
    for email in special_char_emails:
        assert validate_email(email) is True, f"{email} should be valid"