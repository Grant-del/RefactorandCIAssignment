# test_node.py

from src.node import Node

def test_node_creation():
    node = Node(10)
    assert node.get_element() == 10

def test_node_set_element():
    node = Node(5)
    node.set_element(15)
    assert node.get_element() == 15

def test_node_set_previous():
    node1 = Node(10)
    node2 = Node(20)
    node1.set_previous(node2)
    assert node1.get_previous() == node2

def test_node_set_next():
    node1 = Node(10)
    node2 = Node(20)
    node1.set_next(node2)
    assert node1.get_next() == node2

# Add more test cases as needed
