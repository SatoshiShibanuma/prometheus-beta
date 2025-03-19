def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A magic square is a 3x3 grid where:
    - Contains exactly 9 or 10 numbers 
    - Numbers are unique and in range 1-9
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
    
    # Extract grid numbers with flexible separator handling
    if len(numbers) == 10:
        # Try different strategies to extract 9 unique grid numbers
        test_sets = [
            # Strategy 1: Remove last number
            sorted(set(numbers[:-1])),
            # Strategy 2: Remove if matches a grid number
            sorted(set([n for n in numbers if n != numbers[-1]])),
            # Strategy 3: Full list
            sorted(set(numbers))
        ]
        
        for test_numbers in test_sets:
            # Validate each possibility
            if (len(test_numbers) == 9 and 
                set(test_numbers) == set(range(1, 10)) and 
                _validate_magic_square(test_numbers)):
                return True
        return False
    
    # For 9 numbers, validate directly
    if (len(set(numbers)) == 9 and 
        set(numbers) == set(range(1, 10)) and 
        _validate_magic_square(numbers)):
        return True
    
    return False

def _validate_magic_square(grid_numbers):
    """
    Internal helper function to validate magic square grid.
    
    Args:
        grid_numbers (list): 9 unique numbers in range 1-9
    
    Returns:
        bool: True if the grid represents a valid magic square, False otherwise
    """
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