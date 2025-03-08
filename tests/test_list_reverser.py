import pytest
from src.list_reverser import reverse_list_with_stack, Stack

def test_stack_basic_operations():
    """Test basic Stack data structure operations."""
    stack = Stack()
    
    # Test initial state
    assert stack.is_empty() == True
    
    # Test push and pop
    stack.push(1)
    assert stack.is_empty() == False
    assert stack.pop() == 1
    assert stack.is_empty() == True
    
    # Test multiple push and pop
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty() == True

def test_stack_empty_pop_raises_error():
    """Test that popping from an empty stack raises an IndexError."""
    stack = Stack()
    with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
        stack.pop()

def test_reverse_list_basic():
    """Test reversing a simple list of integers."""
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_list_empty():
    """Test reversing an empty list."""
    assert reverse_list_with_stack([]) == []

def test_reverse_list_single_element():
    """Test reversing a list with a single element."""
    input_list = [42]
    assert reverse_list_with_stack(input_list) == [42]

def test_reverse_list_different_types():
    """Test reversing a list with different types of elements."""
    input_list = [1, "hello", 3.14, True]
    expected = [True, 3.14, "hello", 1]
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_list_large():
    """Test reversing a large list to ensure performance."""
    input_list = list(range(1000))
    expected = list(reversed(input_list))
    assert reverse_list_with_stack(input_list) == expected