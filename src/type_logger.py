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
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Get the type of the variable
    var_type = type(variable)
    
    # Log the type
    logging.info(f'Variable type: {var_type}')
    
    # Return the type as a string for potential further use
    return var_type.__name__