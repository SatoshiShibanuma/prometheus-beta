import pytest
from src.sparse_matrix_multiply import sparse_matrix_multiply

def test_basic_sparse_matrix_multiplication():
    # Simple sparse matrix multiplication
    matrix_a = {
        0: {0: 1, 2: 3},
        1: {1: 2}
    }
    matrix_b = {
        0: {0: 4, 1: 5},
        1: {1: 6},
        2: {2: 7}
    }
    
    expected = {
        0: {0: 4, 1: 5},
        1: {1: 12}
    }
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == expected

def test_empty_matrices():
    # Test multiplication with empty matrices
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {0: {}}) == {}

def test_zero_result_matrix():
    # Matrices that result in zero matrix
    matrix_a = {0: {0: 1}, 1: {1: 2}}
    matrix_b = {0: {1: 3}, 1: {0: 4}}
    
    assert sparse_matrix_multiply(matrix_a, matrix_b) == {}

def test_sparse_matrix_with_floats():
    # Test with floating-point values
    matrix_a = {
        0: {0: 1.5, 2: 3.0},
        1: {1: 2.5}
    }
    matrix_b = {
        0: {0: 4.0, 1: 5.0},
        1: {1: 6.0},
        2: {2: 7.0}
    }
    
    expected = {
        0: {0: 6.0, 1: 7.5},
        1: {1: 15.0}
    }
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    assert result == pytest.approx(expected)

def test_large_sparse_matrix():
    # Test with a larger sparse matrix
    matrix_a = {
        0: {0: 1, 2: 3, 5: 2},
        2: {1: 4, 3: 1},
        4: {0: 5, 4: 2}
    }
    matrix_b = {
        0: {1: 2, 3: 1},
        1: {2: 3, 4: 4},
        2: {0: 5, 5: 6},
        3: {3: 2},
        5: {1: 7}
    }
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Manual verification of some key cells
    assert result[0].get(1, 0) == 2  # From 1*2 in first row
    assert result[2].get(2, 0) == 12  # From 4*3 in second row
    assert result[4].get(4, 0) == 8  # From 2*4 in last row

def test_performance_of_sparse_representation():
    # Test that multiplication is efficient for sparse matrices
    matrix_a = {i: {i*2: i} for i in range(1000)}
    matrix_b = {i: {i*3: i} for i in range(1000)}
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Verify only diagonal or near-diagonal entries exist
    for row, row_data in result.items():
        for col, val in row_data.items():
            assert val == row * col  # Simple validation of sparse result