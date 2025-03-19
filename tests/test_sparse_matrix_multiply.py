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
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Verify specific elements
    assert result[0][0] == 4
    assert result.get(1, {}).get(1) == 12
    # Verify no unexpected elements
    assert len(result.get(0, {})) <= 2
    assert len(result.get(1, {})) == 1

def test_empty_matrices():
    # Test multiplication with empty matrices
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {0: {}}) == {}

def test_zero_result_matrix():
    # Matrices that result in essentially zero matrix
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
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Check specific values with approx
    assert result[0][0] == pytest.approx(6.0)
    assert result[0][1] == pytest.approx(7.5)
    assert result[1][1] == pytest.approx(15.0)

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
    
    # More specific checks
    assert all(abs(val) > 1e-10 for row in result.values() for val in row.values())

def test_very_sparse_performance():
    # Test performance and sparsity for very sparse matrices
    matrix_a = {i: {i*2: 1} for i in range(100) if i*2 < 200}
    matrix_b = {i: {i*3: 1} for i in range(100) if i*3 < 300}
    
    result = sparse_matrix_multiply(matrix_a, matrix_b)
    
    # Verify result is truly sparse
    assert len(result) < 50  # Much smaller than full matrix would be
    # Ensure only diagonal-like entries exist
    for row, row_data in result.items():
        for col, val in row_data.items():
            assert abs(val - 1) < 1e-10  # Only 1's should exist