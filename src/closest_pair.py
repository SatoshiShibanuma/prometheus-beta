def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers to find the closest pair from.
    
    Returns:
        tuple: A tuple containing two numbers that are closest to each other.
               If multiple pairs have the same smallest difference, 
               return the pair with the smallest numbers.
    
    Raises:
        ValueError: If the input list has fewer than 2 numbers.
    """
    # Check for valid input
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    # If all input is the same, return that pair
    if len(set(numbers)) == 1:
        return (numbers[0], numbers[0])
    
    # Create a complete list of pair differences
    pair_diffs = []
    sorted_nums = sorted(numbers)
    
    for i in range(len(sorted_nums) - 1):
        pair_diffs.append((abs(sorted_nums[i] - sorted_nums[i+1]), 
                           sorted_nums[i], 
                           sorted_nums[i+1]))
    
    # Sort by difference, then by the first number, then the second
    pair_diffs.sort(key=lambda x: (x[0], x[1], x[2]))
    
    # Return the pair of numbers from the first (smallest) pair
    return (pair_diffs[0][1], pair_diffs[0][2])