import os
import pytest
import getpass
from src.file_owner import get_file_owner

def test_get_file_owner_current_user():
    """Test getting owner of a file owned by current user."""
    # Create a test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    try:
        # Get current username
        current_user = getpass.getuser()
        
        # Check if file owner matches current user
        assert get_file_owner(test_file_path) == current_user
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_get_file_owner_nonexistent_file():
    """Test handling of nonexistent file."""
    with pytest.raises(FileNotFoundError):
        get_file_owner('non_existent_file.txt')

def test_get_file_owner_input_types():
    """Test various input types for file path."""
    # Relative path
    relative_file_path = './README.md'
    assert isinstance(get_file_owner(relative_file_path), str)
    
    # Absolute path
    absolute_file_path = os.path.abspath('README.md')
    assert isinstance(get_file_owner(absolute_file_path), str)
    
    # Use README.md expanded path
    user_path = os.path.expanduser('~/README.md') if os.path.exists(os.path.expanduser('~/README.md')) else './README.md'
    assert isinstance(get_file_owner(user_path), str)

def test_get_file_owner_return_type():
    """Verify that the function returns a string."""
    result = get_file_owner('README.md')
    assert isinstance(result, str)
    assert len(result) > 0