import pytest
from src.parity_subsequence import find_longest_parity_subsequence

def test_mixed_parity_sequence():
    # Test a sequence with mixed parities
    arr = [1, 3, 2, 4, 5]
    assert find_longest_parity_subsequence(arr) == [1, 3, 5]

def test_all_even_sequence():
    # Test a sequence of all even numbers
    arr = [2, 4, 6, 8, 10]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6, 8, 10]

def test_all_odd_sequence():
    # Test a sequence of all odd numbers
    arr = [1, 3, 5, 7, 9]
    assert find_longest_parity_subsequence(arr) == [1, 3, 5, 7, 9]

def test_empty_sequence():
    # Test empty input
    arr = []
    assert find_longest_parity_subsequence(arr) == []

def test_single_element_sequences():
    # Test single even and odd elements
    assert find_longest_parity_subsequence([1]) == [1]
    assert find_longest_parity_subsequence([2]) == [2]

def test_complex_mixed_sequence():
    # Test a more complex mixed sequence
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6, 8, 10, 12]

def test_sequence_with_breaks():
    # Test a sequence with breaks in parity
    arr = [2, 4, 5, 6, 8, 9, 10, 11, 12, 14]
    assert find_longest_parity_subsequence(arr) == [2, 4, 6, 8, 10, 12, 14]

def test_negative_numbers():
    # Test with negative numbers
    arr = [-1, -3, -2, -4, -5]
    assert find_longest_parity_subsequence(arr) == [-1, -3, -5]