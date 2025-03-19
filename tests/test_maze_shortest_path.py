import pytest
from src.maze_shortest_path import find_shortest_path

def test_basic_path_exists():
    """Test a simple maze with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 5

def test_no_path_blocked_start():
    """Test when start is blocked"""
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_no_path_blocked_end():
    """Test when end is blocked"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert find_shortest_path(grid) == -1

def test_single_cell_grid():
    """Test a single cell grid"""
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_no_path_completely_blocked():
    """Test a grid with no possible path"""
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]
    assert find_shortest_path(grid) == -1

def test_larger_grid_with_path():
    """Test a larger grid with a path"""
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert find_shortest_path(grid) == 7

def test_empty_grid_raises_error():
    """Test that empty grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path([])

def test_none_grid_raises_error():
    """Test that None grid raises ValueError"""
    with pytest.raises(ValueError):
        find_shortest_path(None)