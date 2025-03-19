def is_magic_square(numbers):
    """
    Determine if a list of 9 or 10 integers represents a valid 3x3 magic square.
    
    A magic square is a 3x3 grid where:
    - Contains exactly 9 or 10 numbers 
    - Has 9 unique numbers in range 1-9
    - All rows, columns, and diagonals sum to the same magic constant (15)
    
    Args:
        numbers (list): A list of 9 or 10 integers to check
    
    Returns:
        bool: True if the list represents a valid 3x3 magic square, False otherwise
    
    Raises:
        ValueError: If input is not a list
    """
    # Validate input
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    
    # Check for correct length (9 or 10 numbers)
    if len(numbers) not in [9, 10]:
        return False
    
    # If 10 numbers, try to filter out the separator
    if len(numbers) == 10:
        # Use set to remove duplicates and sort to ensure consistent handling
        filtered_numbers = sorted(set(n for n in numbers if 1 <= n <= 9))
        
        # Ensure we end up with exactly 9 unique numbers
        if len(filtered_numbers) != 9:
            return False
    else:
        # For 9 numbers, use the list directly
        filtered_numbers = sorted(numbers)
    
    # Validate unique numbers in range 1-9
    if set(filtered_numbers) != set(range(1, 10)):
        return False
    
    # Reshape the list into a 3x3 grid
    grid = [
        filtered_numbers[0:3],
        filtered_numbers[3:6],
        filtered_numbers[6:9]
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