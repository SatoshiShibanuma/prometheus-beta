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
    Test that tree structure is consistent regardless of insertion order.
    """
    bst1 = BinarySearchTree()
    bst1.insert(5)
    bst1.insert(3)
    bst1.insert(7)
    
    bst2 = BinarySearchTree()
    bst2.insert(7)
    bst2.insert(3)
    bst2.insert(5)
    
    # Verify bst1 structure
    assert bst1.root.key == 5
    assert bst1.root.left.key == 3
    assert bst1.root.right.key == 7
    
    # Verify bst2 structure
    assert bst2.root.key == 5
    assert bst2.root.left.key == 3
    assert bst2.root.right.key == 7