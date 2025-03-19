def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A magic square is a 3x3 grid where:
    - Contains exactly 10 numbers (9 grid numbers + optional separator)
    - Numbers are unique and in range 1-9
    - All rows, columns, and diagonals sum to the same magic constant (15)
    
    Args:
        numbers (list): A list of 10 integers to check
    
    Returns:
        bool: True if the list represents a valid 3x3 magic square, False otherwise
    
    Raises:
        ValueError: If input is not a list of 10 integers
    """
    # Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    # Check for correct length (10 numbers)
    if len(numbers) != 10:
        return False
    
    # Optional: remove the separator number if present
    if len(set(numbers)) == 10:
        # If all 10 numbers are unique, remove the last number (separator)
        grid_numbers = sorted(numbers[:-1])
    else:
        grid_numbers = sorted(numbers)
    
    # Validate grid requirements
    if len(grid_numbers) != 9:
        return False
    
    # Check unique numbers in range 1-9
    if set(grid_numbers) != set(range(1, 10)):
        return False
    
    # Reshape the list into a 3x3 grid
    grid = [
        grid_numbers[0:3],
        grid_numbers[3:6],
        grid_numbers[6:9]
    ]
    
    # Magic constant for 3x3 magic square is always 15
    magic_constant = 15
    
    # Check rows
    for row in grid:
        if sum(row) != magic_constant:
            return False
    
    # Check columns
    for col in range(3):
        column_sum = grid[0][col] + grid[1][col] + grid[2][col]
        if column_sum != magic_constant:
            return False
    
    # Check diagonals
    diag1_sum = grid[0][0] + grid[1][1] + grid[2][2]
    diag2_sum = grid[0][2] + grid[1][1] + grid[2][0]
    
    return diag1_sum == magic_constant and diag2_sum == magic_constant