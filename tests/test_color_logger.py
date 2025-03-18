import sys
import io
import pytest
from src.color_logger import log_colored_message

def test_log_default_message():
    """Test logging a message without a color."""
    output = io.StringIO()
    log_colored_message("Hello World", file=output)
    assert output.getvalue().strip() == "Hello World"

def test_log_colored_message():
    """Test logging a message with different colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    for color in colors:
        output = io.StringIO()
        log_colored_message("Test Message", color=color, file=output)
        result = output.getvalue().strip()
        assert result.startswith('\033[9')
        assert result.endswith('\033[0m')

def test_log_none_message():
    """Test that logging None raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be None"):
        log_colored_message(None)

def test_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid color"):
        log_colored_message("Test", color="purple")

def test_color_order():
    """Verify color codes are applied correctly."""
    output = io.StringIO()
    log_colored_message("Test", color="red", file=output)
    result = output.getvalue().strip()
    assert result.startswith('\033[91m')
    assert result.endswith('\033[0m')