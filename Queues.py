class QueueList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued = {removed}")
            return removed
        else:
            print("Queue is empty!!!")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty!!!")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print(f"Queue State: {self.queue}")


if __name__ == "__main__":
    q = QueueList()
    while True:
        print("\nQueued Operations")
        print("1. Enqueue")
        print("2. Dequeued")
        print("3. peek")
        print("4. Display")
        print("5. Size")
        print("6. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            item = int(input("Enter the item to enqueued"))
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            print("Front Element:", q.peek())
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Queue size:", q.size())
        elif choice == 6:
            break
        else:
            print("Invalid Choice Please Enter A Valid Choice")
