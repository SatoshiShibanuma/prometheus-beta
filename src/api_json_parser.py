import json
from typing import Dict, Any, Union

def parse_api_json_response(response: Union[str, bytes, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Parse a JSON response from an API, handling various input types.

    Args:
        response (Union[str, bytes, Dict[str, Any]]): The API response to parse.
            Can be a JSON string, bytes, or already parsed dictionary.

    Returns:
        Dict[str, Any]: A parsed dictionary containing the API response data.

    Raises:
        ValueError: If the input cannot be parsed as JSON.
        TypeError: If the input is not a supported type.
    """
    # If already a dictionary, return as-is
    if isinstance(response, dict):
        return response

    # If bytes, decode to string
    if isinstance(response, bytes):
        response = response.decode('utf-8')

    # If string, parse JSON
    if isinstance(response, str):
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    # If not a supported type, raise TypeError
    raise TypeError(f"Unsupported response type: {type(response)}")