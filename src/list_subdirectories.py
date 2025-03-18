import os
from typing import List

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in the given directory.

    Args:
        directory_path (str): Path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # Get all subdirectories
    try:
        # Use list comprehension to filter only directories
        subdirs = [
            d for d in os.listdir(directory_path) 
            if os.path.isdir(os.path.join(directory_path, d))
        ]
        return subdirs
    except PermissionError:
        raise PermissionError(f"Permission denied to access directory: {directory_path}")