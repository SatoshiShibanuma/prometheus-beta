import os
import pytest
import tarfile
import tempfile
import shutil


from src.tar_extractor import extract_tar_archive


@pytest.fixture
def sample_tar_archive():
    """Create a sample tar archive for testing."""
    temp_dir = tempfile.mkdtemp()
    
    # Create some test files
    test_files = {
        'file1.txt': 'Content of file 1',
        'file2.txt': 'Content of file 2',
        'nested/file3.txt': 'Content of nested file'
    }
    
    # Prepare directories
    for filepath in test_files:
        full_path = os.path.join(temp_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(test_files[filepath])
    
    # Create tar archive
    tar_path = os.path.join(temp_dir, 'test_archive.tar')
    with tarfile.open(tar_path, 'w') as tar:
        for filepath in test_files:
            tar.add(os.path.join(temp_dir, filepath), arcname=filepath)
    
    yield tar_path
    
    # Cleanup
    shutil.rmtree(temp_dir)


def test_extract_all_files(sample_tar_archive):
    """Test extracting all files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(sample_tar_archive, extract_dir)
        
        assert len(extracted) == 3
        assert all(os.path.exists(path) for path in extracted)


def test_extract_specific_files(sample_tar_archive):
    """Test extracting specific files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(
            sample_tar_archive, 
            extract_dir, 
            files_to_extract='file1.txt'
        )
        
        assert len(extracted) == 1
        assert os.path.basename(extracted[0]) == 'file1.txt'


def test_extract_multiple_specific_files(sample_tar_archive):
    """Test extracting multiple specific files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(
            sample_tar_archive, 
            extract_dir, 
            files_to_extract=['file1.txt', 'nested/file3.txt']
        )
        
        assert len(extracted) == 2
        assert sorted([os.path.basename(path) for path in extracted]) == ['file1.txt', 'file3.txt']


def test_extract_nonexistent_file(sample_tar_archive):
    """Test extracting a file that doesn't exist in the archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted = extract_tar_archive(
            sample_tar_archive, 
            extract_dir, 
            files_to_extract='nonexistent.txt'
        )
        
        assert len(extracted) == 0


def test_extract_to_default_location(sample_tar_archive):
    """Test extracting files to the default location."""
    extracted = extract_tar_archive(sample_tar_archive)
    
    assert len(extracted) == 3
    assert all(os.path.exists(path) for path in extracted)
    assert all(os.path.dirname(path) == os.path.dirname(sample_tar_archive) for path in extracted)


def test_raise_file_not_found():
    """Test raising FileNotFoundError for non-existent tar file."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')