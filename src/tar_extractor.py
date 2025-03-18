import os
import tarfile
from typing import Union, List, Optional


def extract_tar_archive(
    tar_path: str, 
    extract_path: Optional[str] = None, 
    files_to_extract: Optional[Union[str, List[str]]] = None
) -> List[str]:
    """
    Extract files from a tar archive with flexible extraction options.

    Args:
        tar_path (str): Path to the tar archive file.
        extract_path (Optional[str], optional): Destination directory for extraction. 
                                                Defaults to the tar file's directory.
        files_to_extract (Optional[Union[str, List[str]]], optional): 
            Specific files to extract. Can be a single filename or a list of filenames.
            If None, extracts all files in the archive.

    Returns:
        List[str]: Paths of extracted files.

    Raises:
        FileNotFoundError: If the tar archive does not exist.
        tarfile.TarError: For tar-related processing errors.
        ValueError: For invalid input parameters.
    """
    # Validate input tar path
    tar_path = os.path.abspath(tar_path)  # Ensure absolute path
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")

    # Always use tar file's directory as default
    extract_path = os.path.dirname(tar_path)

    # Ensure extraction directory exists
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Normalize files_to_extract to a list
    if files_to_extract is None:
        files_to_extract = []
    elif isinstance(files_to_extract, str):
        files_to_extract = [files_to_extract]

    # Track extracted files
    extracted_files = []

    try:
        with tarfile.open(tar_path, 'r:*') as tar:
            # If no specific files specified, extract all
            if not files_to_extract:
                tar.extractall(path=extract_path)
                extracted_files = [
                    os.path.join(extract_path, name) 
                    for name in tar.getnames()
                ]
            else:
                # Extract specific files
                for file in files_to_extract:
                    try:
                        tar.extract(file, path=extract_path)
                        extracted_files.append(
                            os.path.join(extract_path, file)
                        )
                    except KeyError:
                        # Skip files not in archive
                        continue

        return extracted_files

    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error processing tar archive: {e}")