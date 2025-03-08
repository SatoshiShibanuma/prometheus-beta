def solve_n_queens(n):
    """
    Solve the N-Queens problem for a given board size.
    
    Args:
        n (int): Size of the chessboard and number of queens to place.
    
    Returns:
        list: A list of solutions, where each solution is a list of queen positions.
              Each position is represented as a list [row, col].
    
    Raises:
        ValueError: If n is less than 1 or the problem is unsolvable.
    """
    # Input validation
    if not isinstance(n, int) or n < 1:
        raise ValueError("Board size must be a positive integer")
    
    # Special case: 1x1 board has a trivial solution
    if n == 1:
        return [[[0, 0]]]
    
    # Optimization: N-Queens only has solutions for n >= 4
    if n < 4:
        return []
    
    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col] safely.
        
        Args:
            board (list): Current board state with queen positions
            row (int): Row to check
            col (int): Column to check
        
        Returns:
            bool: True if queen can be placed safely, False otherwise
        """
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on the left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve_recursively(board, col):
        """
        Recursive backtracking method to solve N-Queens problem.
        
        Args:
            board (list): Current board state 
            col (int): Current column being processed
        
        Returns:
            list: List of solutions found
        """
        # Base case: all queens are placed
        if col >= n:
            solutions = []
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            return [solution]
        
        solutions = []
        
        # Try placing queen in each row of the current column
        for row in range(n):
            # Check if queen can be placed safely
            if is_safe(board, row, col):
                # Place the queen
                board[row][col] = 1
                
                # Recur to place rest of the queens
                sub_solutions = solve_recursively(board, col + 1)
                solutions.extend(sub_solutions)
                
                # Backtrack: remove queen from current position
                board[row][col] = 0
        
        return solutions
    
    # Initialize empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Solve and return all solutions
    return solve_recursively(board, 0)

# Optional: function to print solutions for visualization
def print_board(solution, n):
    """
    Print a visual representation of a N-Queens solution.
    
    Args:
        solution (list): A single solution of queen positions
        n (int): Board size
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in solution:
        board[row][col] = 'Q'
    
    for row in board:
        print(' '.join(row))
    print()  # Extra newline for spacing