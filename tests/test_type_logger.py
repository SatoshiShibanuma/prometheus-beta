"""
Tests for the type_logger module.
"""

import pytest
import logging
import io
import sys
from src.type_logger import log_variable_type

def test_log_variable_type_integer():
    """Test logging type for an integer."""
    # Redirect logging to capture output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call the function
    result = log_variable_type(42)
    
    # Check the return value
    assert result == 'int'
    
    # Check the log output
    log_output = log_capture.getvalue()
    assert 'Variable type: <class \'int\'>' in log_output

def test_log_variable_type_string():
    """Test logging type for a string."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    result = log_variable_type("hello")
    
    assert result == 'str'
    log_output = log_capture.getvalue()
    assert 'Variable type: <class \'str\'>' in log_output

def test_log_variable_type_list():
    """Test logging type for a list."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    result = log_variable_type([1, 2, 3])
    
    assert result == 'list'
    log_output = log_capture.getvalue()
    assert 'Variable type: <class \'list\'>' in log_output

def test_log_variable_type_none():
    """Test logging type for None."""
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    result = log_variable_type(None)
    
    assert result == 'NoneType'
    log_output = log_capture.getvalue()
    assert 'Variable type: <class \'NoneType\'>' in log_output

def test_log_variable_type_custom_class():
    """Test logging type for a custom class."""
    class TestClass:
        pass
    
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    test_instance = TestClass()
    result = log_variable_type(test_instance)
    
    assert result == 'TestClass'
    log_output = log_capture.getvalue()
    assert 'Variable type: <class \'TestClass\'>' in log_output