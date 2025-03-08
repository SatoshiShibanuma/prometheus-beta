from typing import List, TypeVar

T = TypeVar('T')

class Stack:
    """
    A simple Stack implementation with basic operations.
    
    This implementation provides O(1) time complexity for push and pop operations,
    and uses a list as the underlying data structure.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item: T) -> None:
        """
        Add an item to the top of the stack.
        
        Args:
            item (T): The item to be added to the stack.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self._items.append(item)
    
    def pop(self) -> T:
        """
        Remove and return the top item from the stack.
        
        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self._items:
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self._items) == 0

def reverse_list_with_stack(input_list: List[T]) -> List[T]:
    """
    Reverse a list using a Stack data structure.
    
    This function handles lists of any length, including empty and single-element lists.
    It uses a stack to efficiently reverse the list in-place.
    
    Args:
        input_list (List[T]): The input list to be reversed.
    
    Returns:
        List[T]: A new list with elements in reversed order.
    
    Time Complexity: O(n), where n is the length of the input list
    Space Complexity: O(n) for the additional stack
    
    Examples:
        >>> reverse_list_with_stack([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1]
        >>> reverse_list_with_stack([])
        []
        >>> reverse_list_with_stack([42])
        [42]
    """
    # Handle edge cases
    if not input_list:
        return []
    
    # Create a stack
    stack = Stack()
    
    # Push all elements to the stack
    for item in input_list:
        stack.push(item)
    
    # Create a new list by popping from the stack
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list