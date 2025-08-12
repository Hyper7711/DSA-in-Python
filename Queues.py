"""Queue implementation using Python lists."""


class QueueList:
    """A simple Queue implementation using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the queue."""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        print("Queue is empty!")
        return None

    def peek(self):
        """Return the front item of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        print("Queue is empty!")
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)

    def display(self):
        """Display the current state of the queue."""
        print("Queue state:", self.queue)


if __name__ == "__main__":
    q = QueueList()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_input = int(
                input("Enter the item to enqueue: ")
            )  # Renamed 'item' to 'user_input'
            q.enqueue(user_input)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            print("Front Element:", q.peek())
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Queue Size:", q.size())
        elif choice == 6:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
