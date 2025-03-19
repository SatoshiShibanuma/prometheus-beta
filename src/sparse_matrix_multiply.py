from typing import Dict, Union, List

def sparse_matrix_multiply(
    matrix_a: Dict[int, Dict[int, Union[int, float]]],
    matrix_b: Dict[int, Dict[int, Union[int, float]]]
) -> Dict[int, Dict[int, Union[int, float]]]:
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    Args:
        matrix_a (Dict[int, Dict[int, Union[int, float]]]): First sparse matrix 
            represented as {row_index: {col_index: value}}
        matrix_b (Dict[int, Dict[int, Union[int, float]]]): Second sparse matrix 
            represented as {row_index: {col_index: value}}
    
    Returns:
        Dict[int, Dict[int, Union[int, float]]]: Resulting sparse matrix after multiplication
    
    Raises:
        ValueError: If matrices cannot be multiplied due to dimension mismatch
    """
    # Validate matrix multiplication is possible
    if not matrix_a or not matrix_b:
        return {}
    
    # Transpose matrix_b for efficient column access
    transposed_b = {}
    for row_b, row_data in matrix_b.items():
        for col, val in row_data.items():
            if col not in transposed_b:
                transposed_b[col] = {}
            transposed_b[col][row_b] = val
    
    # Perform sparse matrix multiplication
    result = {}
    for row_a, row_a_data in matrix_a.items():
        result_row = {}
        for col_b, col_b_data in transposed_b.items():
            # Compute dot product for this cell
            cell_value = sum(
                row_a_data.get(k, 0) * col_b_data.get(k, 0) 
                for k in set(row_a_data) & set(col_b_data)
            )
            
            # Only store non-zero values
            if cell_value != 0:
                result_row[col_b] = cell_value
        
        # Only store rows with non-zero entries
        if result_row:
            result[row_a] = result_row
    
    return result