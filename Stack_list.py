class Stack:
    def __init__(self):
        self.stack = []  # initialize an empty stack

    def push(self, item):
        self.stack.append(item)  # adding item at the top
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.is_empty():  # Remove and return at the top
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        return self.stack.pop()

    def peek(self):  # return to the top without removing it
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.stack[-1]

    def is_empty(self):  # checks is the stack is empty
        return len(self.stack) == 0

    def size(self):  # return the number of item of the stack
        return len(self.stack)

    def display(self):  # Display is the stack is empty
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Current Stack (top to bottom):", self.stack[::-1])


# Example :
if __name__ == "__main__":
    stack = Stack()

    # Performing stack operations
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Top element is:", stack.peek())
    print("Popped element is:", stack.pop())
    stack.display()
    print("Is the stack empty?", stack.is_empty())
    print("Stack size:", stack.size())
