# test_doubly_linked_list.py

from src.linkedList import DoublyLinkedList, Node

def test_doubly_linked_list_creation():
    dll = DoublyLinkedList()
    assert dll.size() == 0
    assert dll.is_empty() == True

def test_doubly_linked_list_add_last():
    dll = DoublyLinkedList()
    dll.add_last(Node(10))
    assert dll.size() == 1
    assert dll.is_empty() == False

def test_doubly_linked_list_add_first():
    dll = DoublyLinkedList()
    dll.add_first(Node(10))
    assert dll.size() == 1
    assert dll.is_empty() == False

# Add more test cases as needed
