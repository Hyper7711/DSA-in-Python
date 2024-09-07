# Define a Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        # Each node will store data and a pointer to the next node
        self.data = data  # Store the data value of the node
        self.next = None  # Initialize the next pointer to None
        

# Define the CircularLinkedList class to manage the linked list operations
class CircularLinkedList:
    def __init__(self):
        # Initially, the list is empty, so head is set to None
        self.head = None

    # Method to add a new node at the end of the circular linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty
            self.head = new_node  # Make the new node the head
            new_node.next = self.head  # Point it to itself to form a circle
        else:
            temp = self.head
            # Traverse to the last node (whose next is the head)
            while temp.next != self.head:
                temp = temp.next
            # Insert the new node at the end and point it to the head
            temp.next = new_node
            new_node.next = self.head

    # Method to display the circular linked list
    def display(self):
        if not self.head:  # If the list is empty, just return
            print("The list is empty.")
            return
        temp = self.head
        # Traverse and print each node's data until we reach the head again
        while True:
            print(temp.data, end=" ")  # Print the data of the current node
            temp = temp.next  # Move to the next node
            if temp == self.head:  # Stop when we return to the head
                break
        print()  # For a clean output

# Driver code to demonstrate the functionality
cll = CircularLinkedList()  # Create an empty circular linked list
cll.append(10)  # Append 10 to the list
cll.append(20)  # Append 20 to the list
cll.append(30)  # Append 30 to the list

cll.display()  # Display the list: Output will be 10 20 30
