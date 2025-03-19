import pytest
from src.binary_tree import TreeNode, dfs_inorder_traversal

def test_empty_tree():
    """Test DFS traversal on an empty tree."""
    assert dfs_inorder_traversal(None) == []

def test_single_node_tree():
    """Test DFS traversal on a tree with a single node."""
    root = TreeNode(5)
    assert dfs_inorder_traversal(root) == [5]

def test_balanced_tree():
    """Test DFS traversal on a balanced binary tree."""
    #     4
    #   /   \
    #  2     6
    # / \   / \
    #1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    
    assert dfs_inorder_traversal(root) == [1, 2, 3, 4, 5, 6, 7]

def test_left_skewed_tree():
    """Test DFS traversal on a left-skewed tree."""
    #   3
    #  /
    # 2
    # /
    #1
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    
    assert dfs_inorder_traversal(root) == [1, 2, 3]

def test_right_skewed_tree():
    """Test DFS traversal on a right-skewed tree."""
    #1
    # \
    #  2
    #   \
    #    3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    assert dfs_inorder_traversal(root) == [1, 2, 3]

def test_invalid_input():
    """Test that TypeError is raised for invalid input."""
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_inorder_traversal("not a tree")
    
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_inorder_traversal(42)