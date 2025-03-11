import pytest
import logging
import emoji
from src.emoji_logger import log_with_emojis

def test_log_with_emojis_default(caplog):
    """Test logging with default parameters"""
    caplog.set_level(logging.INFO)
    result = log_with_emojis("Test message")
    assert result == "Test message"
    assert "Test message" in caplog.text

def test_log_with_specific_emoji(caplog):
    """Test logging with a specific emoji"""
    caplog.set_level(logging.INFO)
    result = log_with_emojis("Happy day", ":smile:")
    assert emoji.emojize(":smile:", language='alias') in result
    assert "Happy day" in result
    assert result in caplog.text

def test_log_with_unicode_emoji(caplog):
    """Test logging with a unicode emoji"""
    caplog.set_level(logging.INFO)
    result = log_with_emojis("Celebration", "🎉")
    assert "🎉 Celebration" == result
    assert result in caplog.text

def test_different_log_levels(caplog):
    """Test different logging levels"""
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in log_levels:
        caplog.clear()
        caplog.set_level(getattr(logging, level.upper()))
        result = log_with_emojis("Test message", log_level=level)
        assert result == "Test message"
        assert "Test message" in caplog.text

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_with_emojis("Test message", log_level="invalid")

def test_invalid_message_type():
    """Test that non-string message raises a TypeError"""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_emojis(123)

def test_fallback_on_invalid_emoji(caplog):
    """Test that an invalid emoji falls back to original message"""
    caplog.set_level(logging.INFO)
    result = log_with_emojis("Test message", "invalid_emoji")
    assert result == "Test message"
    assert "Test message" in caplog.text