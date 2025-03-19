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
    
    # Prepare the grid numbers
    grid_numbers = []
    
    # Handle 10-number case by filtering potential separator
    if len(numbers) == 10:
        # Try to find 9 unique grid numbers
        grid_numbers = sorted([n for n in numbers if 1 <= n <= 9])
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