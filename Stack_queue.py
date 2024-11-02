class DataStructures:
    def __init__(self):
        self.stack = []  # Initialize an empty stack
        self.queue = []  # Initialize an empty queue

    # Stack Operations

    def push_stack(self, value):
        """Adds an element to the top of the stack."""
        self.stack.append(value)
        print(f"Pushed {value} to stack.")

    def pop_stack(self):
        """Removes the element from the top of the stack and returns it."""
        if not self.stack:
            print("Stack is empty.")
            return None
        return self.stack.pop()

    def peek_stack(self):
        """Returns the top element of the stack without removing it."""
        if not self.stack:
            print("Stack is empty.")
            return None
        return self.stack[-1]

    # Queue Operations
    def enqueue_queue(self, value):
        """Adds an element to the end of the queue."""
        self.queue.append(value)
        print(f"Enqueued {value} to queue.")

    def dequeue_queue(self):
        """Removes the element from the front of the queue and returns it."""
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue.pop(0)

    def peek_queue(self):
        """Returns the front element of the queue without removing it."""
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue[0]

    # Display both stack and queue
    def display_structures(self):
        print(f"Stack (Top -> Bottom): {self.stack[::-1]}")
        print(f"Queue (Front -> Rear): {self.queue}")


# Demonstration of Stack and Queue operations
ds = DataStructures()

# Stack Operations
ds.push_stack(10)
ds.push_stack(20)
ds.push_stack(30)
print("Top of Stack:", ds.peek_stack())
print("Popped from Stack:", ds.pop_stack())
ds.display_structures()


# Queue Operations
ds.enqueue_queue(1)
ds.enqueue_queue(2)
ds.enqueue_queue(3)
print("Front of Queue:", ds.peek_queue())
print("Dequeued from Queue:", ds.dequeue_queue())
ds.display_structures()
