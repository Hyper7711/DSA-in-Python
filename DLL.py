# Node class to represent each element in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.prev = None  # Pointer to the previous node, initially None
        self.next = None  # Pointer to the next node, initially None

# Doubly Linked List class to manage nodes
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list, initially None

    # Method to add a node at the front of the list
    def push(self, new_data):
        new_node = Node(new_data)  # Create a new node with the provided data
        new_node.next = self.head  # Set the next of the new node to the current head

        if self.head is not None:  # If the list is not empty
            self.head.prev = new_node  # Update the previous head's prev to the new node

        self.head = new_node  # Move the head to point to the new node

    # Method to print the list from the beginning
    def print_list(self):
        node = self.head  # Start from the head of the list
        while node is not None:  # Traverse the list until you reach at the end
            print(node.data, end=' ')  # Print the data of the current node
            node = node.next  # Move to the next node in the list

# Example usage
dll = DoublyLinkedList()  # Create an empty doubly linked list
dll.push(10)  # Add node with data 10
dll.push(20)  # Add node with data 20
dll.push(30)  # Add node with data 30

dll.print_list()  # Print the list (Output: 30 20 10)

