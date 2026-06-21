class Array:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def delete(self, index):
        self.data.pop(index)

    def access(self, index):
        return self.data[index]

    def display(self):
        print(self.data)


# -----------------------------
# Stack
# -----------------------------
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# -----------------------------
# Queue
# -----------------------------
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# -----------------------------
# Linked List
# -----------------------------
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete(self, key):

        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# -----------------------------
# Test Program
# -----------------------------
if __name__ == "__main__":

    print("\nARRAY")
    arr = Array()
    arr.insert(10)
    arr.insert(20)
    arr.insert(30)
    arr.display()

    print("Access index 1:", arr.access(1))

    arr.delete(1)
    arr.display()

    print("\nSTACK")
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.display()

    print("Pop:", stack.pop())
    stack.display()

    print("\nQUEUE")
    queue = Queue()

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    queue.display()

    print("Dequeue:", queue.dequeue())
    queue.display()

    print("\nLINKED LIST")
    ll = LinkedList()

    ll.insert(100)
    ll.insert(200)
    ll.insert(300)

    ll.traverse()

    ll.delete(200)

    ll.traverse()
