class Node:
    """
    Represents a node in a Binary Search Tree (BST).
    
    Attributes:
        key: The value stored in the node
        left: Reference to the left child node (None if no left child)
        right: Reference to the right child node (None if no right child)
    """
    def __init__(self, key):
        """
        Initialize a new Node with the given key.
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Binary Search Tree data structure with insertion method.
    
    Maintains BST properties:
    1. Left subtree contains only nodes with keys less than the node's key
    2. Right subtree contains only nodes with keys greater or equal to the node's key
    3. Both left and right subtrees are also binary search trees
    """
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root = None
    
    def insert(self, key):
        """
        Insert a new node with the given key into the Binary Search Tree.
        
        If the tree is empty, create the root node.
        Otherwise, find the correct position to insert the new node.
        
        Args:
            key: The value to be inserted into the tree
        
        Returns:
            Node: The newly inserted node
        """
        # If the tree is empty, create the root node
        if self.root is None:
            self.root = Node(key)
            return self.root
        
        # Start at the root and find the correct insertion point
        current = self.root
        while True:
            # If key is less than current node's key, go left
            if key < current.key:
                # If no left child, insert here
                if current.left is None:
                    current.left = Node(key)
                    return current.left
                # Otherwise, continue searching in the left subtree
                current = current.left
            
            # If key is greater or equal to current node's key, go right
            else:
                # If no right child, insert here
                if current.right is None:
                    current.right = Node(key)
                    return current.right
                # Otherwise, continue searching in the right subtree
                current = current.right