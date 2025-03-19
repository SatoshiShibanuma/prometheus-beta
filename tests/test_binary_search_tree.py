import pytest
from src.binary_search_tree import BinarySearchTree, Node

def test_empty_tree_insertion():
    """
    Test inserting into an empty tree creates the root node.
    """
    bst = BinarySearchTree()
    node = bst.insert(5)
    assert bst.root is not None
    assert bst.root.key == 5
    assert bst.root.left is None
    assert bst.root.right is None

def test_multiple_insertions():
    """
    Test inserting multiple nodes maintains BST properties.
    """
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    
    # Verify root
    assert bst.root.key == 5
    
    # Verify left subtree
    assert bst.root.left.key == 3
    assert bst.root.left.left.key == 1
    assert bst.root.left.right.key == 4
    
    # Verify right subtree
    assert bst.root.right.key == 7
    assert bst.root.right.left.key == 6
    assert bst.root.right.right.key == 8

def test_duplicate_key_insertion():
    """
    Test inserting duplicate keys goes to the right subtree.
    """
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(5)
    
    assert bst.root.key == 5
    assert bst.root.right is not None
    assert bst.root.right.key == 5
    assert bst.root.left is None

def test_insertion_order_independence():
    """
    Verify BST properties are maintained regardless of insertion order.
    """
    def validate_bst(bst):
        """
        Helper function to validate BST properties recursively.
        """
        def _is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
            if node is None:
                return True
            
            # Check if current node violates BST property
            if node.key <= min_val or node.key >= max_val:
                return False
            
            # Recursively check left and right subtrees
            return (
                _is_valid_bst(node.left, min_val, node.key) and 
                _is_valid_bst(node.right, node.key, max_val)
            )
        
        return _is_valid_bst(bst.root)
    
    # Test different insertion orders
    insertion_orders = [
        [5, 3, 7],
        [3, 5, 7],
        [7, 5, 3],
        [7, 3, 5]
    ]
    
    for order in insertion_orders:
        bst = BinarySearchTree()
        for value in order:
            bst.insert(value)
        
        # Verify the resulting tree always maintains BST properties
        assert validate_bst(bst), f"BST properties not maintained for insertion order {order}"