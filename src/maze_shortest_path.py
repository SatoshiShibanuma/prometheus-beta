from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path in a 2D grid maze from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
                                The grid is square (NxN).
    
    Returns:
        int: Length of the shortest path from top-left to bottom-right, 
             or -1 if no path exists.
    
    Raises:
        ValueError: If the grid is empty or None.
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Grid dimensions
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Create a visited grid to track explored cells
    visited = [[False] * n for _ in range(n)]
    
    # Queue for BFS, stores (row, col, path_length)
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right corner
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Explore adjacent cells
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                not visited[new_row][new_col]):
                
                queue.append((new_row, new_col, path_length + 1))
                visited[new_row][new_col] = True
    
    # No path found
    return -1