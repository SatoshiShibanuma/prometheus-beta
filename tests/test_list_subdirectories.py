import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories_normal_case():
    """Test listing subdirectories in a normal scenario."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file (should not be included)
        with open(os.path.join(temp_dir, 'somefile.txt'), 'w') as f:
            f.write('test')
        
        # Get subdirectories
        result = list_subdirectories(temp_dir)
        
        # Assert correct subdirectories found
        assert set(result) == {'subdir1', 'subdir2', 'subdir3'}

def test_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_subdirectories(temp_dir)
        assert result == []

def test_nonexistent_directory():
    """Test raising FileNotFoundError for non-existent directory."""
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    """Test raising NotADirectoryError when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)

def test_nested_subdirectories():
    """Test that only immediate subdirectories are returned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create immediate subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'nested_subdir'))
        
        result = list_subdirectories(temp_dir)
        
        # Should only contain immediate subdirectories
        assert result == ['subdir1']