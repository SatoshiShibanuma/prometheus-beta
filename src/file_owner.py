import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by its path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The username of the file owner.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access file metadata.
    """
    # Expand user path and then get absolute path
    full_path = os.path.abspath(os.path.expanduser(file_path))

    # Check if file exists
    if not os.path.exists(full_path):
        # Additional check for expanded paths
        if not os.path.exists(os.path.expanduser(file_path)):
            raise FileNotFoundError(f"File not found: {file_path}")
        # If the original expanded path exists, use it
        full_path = os.path.expanduser(file_path)

    try:
        # Get file stats and retrieve owner's user ID
        file_stat = os.stat(full_path)
        
        # Convert user ID to username
        return pwd.getpwuid(file_stat.st_uid).pw_name
    except PermissionError:
        raise PermissionError(f"Permission denied to access file metadata: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file owner: {str(e)}")