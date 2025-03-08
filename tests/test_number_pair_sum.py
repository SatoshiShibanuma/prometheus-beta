import os
import pytest
from src.number_pair_sum import sum_pairs_with_difference_nine

def test_basic_pairs():
    # Create a test file with numbers that have pairs with difference of 9
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("5\n14\n23\n1\n10\n")
    
    # Pairs with unique indices
    result = sum_pairs_with_difference_nine('tests/test_numbers.txt')
    assert result == (5 + 14) + (1 + 10), "Failed to correctly sum pairs with difference of 9"

def test_multiple_pairs():
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\n5\n14\n23\n32\n")
    
    # Pairs: (1,10), (5,14), (23,32)
    result = sum_pairs_with_difference_nine('tests/test_numbers.txt')
    assert result == (1 + 10) + (5 + 14) + (23 + 32), "Failed to handle multiple pairs"

def test_no_pairs():
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n2\n3\n4\n5\n")
    
    result = sum_pairs_with_difference_nine('tests/test_numbers.txt')
    assert result == 0, "Should return 0 when no pairs exist"

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_difference_nine('non_existent_file.txt')

def test_non_numeric_content():
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n2\nabc\n4\n5\n")
    
    with pytest.raises(ValueError):
        sum_pairs_with_difference_nine('tests/test_numbers.txt')

def test_decimal_numbers():
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("5.5\n14.5\n23.5\n")
    
    # 5.5 and 14.5 form a pair (difference of 9)
    result = sum_pairs_with_difference_nine('tests/test_numbers.txt')
    assert result == (5.5 + 14.5), "Failed to handle decimal numbers"

# Clean up test file after tests
def teardown_module(module):
    try:
        os.remove('tests/test_numbers.txt')
    except FileNotFoundError:
        pass