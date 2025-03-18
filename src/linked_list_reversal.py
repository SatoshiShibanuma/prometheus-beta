class Node:
    """
    Represents a node in a singly linked list.
    
    Attributes:
        value: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, value=None):
        """
        Initialize a new Node.
        
        Args:
            value: The value to be stored in the node (default: None)
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A singly linked list implementation with methods to create, 
    append, and reverse the list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
    
    def append(self, value):
        """
        Append a new node with the given value to the end of the list.
        
        Args:
            value: The value to be added to the list
        """
        new_node = Node(value)
        
        # If the list is empty, set the new node as head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Append the new node
        current.next = new_node
    
    def reverse(self):
        """
        Reverse the order of nodes in the linked list.
        
        Returns:
            LinkedList: The reversed linked list
        """
        # Handle empty list or single node list
        if not self.head or not self.head.next:
            return self
        
        # Initialize pointers for reversal
        prev = None
        current = self.head
        
        # Reverse the links
        while current:
            # Store the next node
            next_node = current.next
            
            # Reverse the current node's pointer
            current.next = prev
            
            # Move pointers one step forward
            prev = current
            current = next_node
        
        # Update head to the last node (now first)
        self.head = prev
        
        return self
    
    def to_list(self):
        """
        Convert the linked list to a Python list for easy comparison.
        
        Returns:
            list: A list of values in the linked list
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


def create_linked_list(n):
    """
    Create a linked list with n nodes, where each node's value is its index.
    
    Args:
        n (int): Number of nodes to create
    
    Returns:
        LinkedList: A linked list with n nodes
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of nodes must be non-negative")
    
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)
    
    return linked_list