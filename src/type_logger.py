"""
Module for logging variable types.

This module provides a utility function to log the type of a given variable.
"""

import logging

def log_variable_type(variable):
    """
    Log the type of a given variable.

    Args:
        variable (Any): The variable whose type is to be logged.

    Returns:
        str: The string representation of the variable's type.

    Example:
        >>> log_variable_type(42)
        # Logs: 'Variable type: <class 'int'>'
        # Returns: 'int'
    """
    # Ensure a logger is used instead of basic config
    logger = logging.getLogger(__name__)
    
    # Ensure the logger has a handler if no handler exists
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    # Get the type of the variable
    var_type = type(variable)
    
    # Log the type
    logger.info(f'Variable type: {var_type}')
    
    # Return the type name, handling both built-in types and custom classes
    type_name = var_type.__name__
    
    # For custom classes, extract just the class name
    if '.' in type_name:
        type_name = type_name.split('.')[-1]
    
    return type_name