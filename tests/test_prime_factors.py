import pytest
from src.prime_factors import get_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization"""
    assert get_prime_factors(12) == [2, 2, 3]
    assert get_prime_factors(15) == [3, 5]
    assert get_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_numbers():
    """Test factorization of prime numbers"""
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(17) == [17]
    assert get_prime_factors(29) == [29]

def test_prime_factors_one():
    """Test factorization of 1"""
    assert get_prime_factors(1) == []

def test_prime_factors_large_number():
    """Test factorization of a larger number"""
    assert get_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        get_prime_factors("12")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_prime_factors(-5)

def test_prime_factors_edge_cases():
    """Test edge cases"""
    # Largest small prime
    assert get_prime_factors(11) == [11]
    
    # Number with repeated prime factors
    assert get_prime_factors(8) == [2, 2, 2]