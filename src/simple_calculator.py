def simple_calculator(num1, num2, operator):
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The arithmetic operation to perform.
                        Supports '+', '-', '*', '/' operations.

    Returns:
        float: Result of the arithmetic operation.

    Raises:
        ValueError: If an invalid operator is provided.
        ZeroDivisionError: If division by zero is attempted.
    """
    # Validate inputs
    if not isinstance(operator, str):
        raise ValueError("Operator must be a string")
    
    # Normalize whitespace and convert operator to stripped version
    operator = operator.strip()

    # Perform arithmetic based on operator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operator: {operator}")