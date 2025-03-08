import pytest
from src.n_queens import solve_n_queens, print_board

def test_solve_n_queens_4x4():
    """Test solution for 4x4 board"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2, "4x4 board should have 2 solutions"
    
    # Validate solutions have correct constraints
    for solution in solutions:
        # Each solution should have 4 queens
        assert len(solution) == 4, "Solution should have 4 queens"
        
        # Check no queens in same row
        rows = [pos[0] for pos in solution]
        assert len(set(rows)) == 4, "No two queens in same row"
        
        # Check no queens in same column
        cols = [pos[1] for pos in solution]
        assert len(set(cols)) == 4, "No two queens in same column"
        
        # Check diagonals: queens have unique row+col and row-col values
        diag1 = [pos[0] + pos[1] for pos in solution]
        diag2 = [pos[0] - pos[1] for pos in solution]
        assert len(set(diag1)) == 4, "No queens on same ascending diagonal"
        assert len(set(diag2)) == 4, "No queens on same descending diagonal"

def test_solve_n_queens_1x1():
    """Test solution for 1x1 board"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1, "1x1 board should have 1 solution"
    assert solutions[0] == [[0, 0]], "1x1 solution should be at [0,0]"

def test_solve_n_queens_small_boards():
    """Test impossibility of solutions for small boards"""
    for n in range(2, 4):
        solutions = solve_n_queens(n)
        assert len(solutions) == 0, f"{n}x{n} board should have no solutions"

def test_solve_n_queens_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Board size must be a positive integer"):
        solve_n_queens(0)
    
    with pytest.raises(ValueError, match="Board size must be a positive integer"):
        solve_n_queens(-1)
    
    with pytest.raises(ValueError, match="Board size must be a positive integer"):
        solve_n_queens("not a number")

def test_solve_n_queens_8x8():
    """Verify expected number of solutions for 8x8 board"""
    solutions = solve_n_queens(8)
    # 8-Queens problem has 92 distinct solutions
    assert len(solutions) == 92, "8x8 board should have 92 solutions"