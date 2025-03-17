import pytest
from src.api_json_parser import parse_api_json_response

def test_parse_json_string():
    json_str = '{"name": "John", "age": 30}'
    result = parse_api_json_response(json_str)
    assert result == {"name": "John", "age": 30}

def test_parse_json_bytes():
    json_bytes = b'{"name": "Jane", "age": 25}'
    result = parse_api_json_response(json_bytes)
    assert result == {"name": "Jane", "age": 25}

def test_parse_existing_dict():
    json_dict = {"name": "Alice", "age": 35}
    result = parse_api_json_response(json_dict)
    assert result == {"name": "Alice", "age": 35}

def test_invalid_json_string():
    with pytest.raises(ValueError, match="Invalid JSON"):
        parse_api_json_response('{"name": "Bob"')  # Intentionally malformed JSON

def test_unsupported_type():
    with pytest.raises(TypeError, match="Unsupported response type"):
        parse_api_json_response(42)  # Non-JSON compatible type

def test_empty_json_string():
    with pytest.raises(ValueError, match="Invalid JSON"):
        parse_api_json_response('')

def test_nested_json():
    nested_json = '{"user": {"name": "Charlie", "details": {"age": 40}}}'
    result = parse_api_json_response(nested_json)
    assert result == {"user": {"name": "Charlie", "details": {"age": 40}}}