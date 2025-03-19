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
        
        for col_b, transposed_col_data in transposed_b.items():
            # Compute dot product for this cell
            cell_value = sum(
                row_a_data.get(k, 0) * transposed_col_data.get(k, 0)
                for k in set(row_a_data) & set(transposed_col_data)
            )
            
            # Only store significantly non-zero values
            if abs(cell_value) > 1e-10:
                result_row[col_b] = cell_value
        
        # Only add non-empty rows with significant non-zero values
        # Trim the row to remove near-zero entries
        cleaned_row = {
            col: val for col, val in result_row.items() 
            if abs(val) > 1e-10
        }
        
        if cleaned_row:
            result[row_a] = cleaned_row
    
    return result