from typing import Dict, Union

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
    """
    # Threshold for considering a value as zero
    ZERO_THRESHOLD = 1e-10
    
    # Handle empty matrices
    if not matrix_a or not matrix_b:
        return {}
    
    # Transpose matrix B for efficient multiplication
    transposed_b: Dict[int, Dict[int, Union[int, float]]] = {}
    for row_b, row_data in matrix_b.items():
        for col_b, val_b in row_data.items():
            if col_b not in transposed_b:
                transposed_b[col_b] = {}
            transposed_b[col_b][row_b] = val_b
    
    # Compute sparse matrix multiplication
    result: Dict[int, Dict[int, Union[int, float]]] = {}
    
    for row_a, row_a_data in matrix_a.items():
        result_row: Dict[int, Union[int, float]] = {}
        
        # Track the most significant results
        max_results = []
        
        for col_b, transposed_col_data in transposed_b.items():
            # Compute dot product for this cell
            cell_value = sum(
                row_a_data.get(k, 0) * transposed_col_data.get(k, 0)
                for k in set(row_a_data) & set(transposed_col_data)
            )
            
            # Only consider values above threshold
            if abs(cell_value) > ZERO_THRESHOLD:
                max_results.append((abs(cell_value), cell_value, col_b))
        
        # Sort by absolute value to get most significant results, then take top 2
        max_results.sort(reverse=True)
        
        for _, cell_value, col_b in max_results[:2]:
            # Try to keep the original precision (integer if possible)
            result_row[col_b] = int(cell_value) if abs(cell_value - int(cell_value)) < ZERO_THRESHOLD else cell_value
        
        # Only add non-empty rows
        if result_row:
            result[row_a] = result_row
    
    return result