class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(value, "inserted into the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
            return

        removed_value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(removed_value, "removed from the queue.")

    def peek(self):
        if self.front is None:
            print("Queue is empty!")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return

        current = self.front
        print("Queue elements:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


queue = LinkedListQueue()

while True:
    print("\n--- Queue Using Linked List ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        queue.enqueue(value)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")