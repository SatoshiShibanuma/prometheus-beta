import pytest
from src.linked_list_reversal import Node, LinkedList, create_linked_list


def test_node_creation():
    """Test Node class instantiation"""
    node = Node(5)
    assert node.value == 5
    assert node.next is None


def test_create_linked_list():
    """Test creating a linked list with specified number of nodes"""
    ll = create_linked_list(5)
    assert ll.to_list() == [0, 1, 2, 3, 4]


def test_create_linked_list_zero_nodes():
    """Test creating a linked list with zero nodes"""
    ll = create_linked_list(0)
    assert ll.to_list() == []


def test_create_linked_list_negative_nodes():
    """Test creating a linked list with negative number of nodes raises ValueError"""
    with pytest.raises(ValueError, match="Number of nodes must be non-negative"):
        create_linked_list(-1)


def test_linked_list_append():
    """Test appending nodes to a linked list"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_linked_list_reverse():
    """Test reversing a linked list"""
    ll = create_linked_list(5)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1, 0]


def test_reverse_empty_list():
    """Test reversing an empty list"""
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []


def test_reverse_single_node_list():
    """Test reversing a list with a single node"""
    ll = LinkedList()
    ll.append(42)
    ll.reverse()
    assert ll.to_list() == [42]