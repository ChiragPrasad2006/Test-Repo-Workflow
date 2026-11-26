class Stack:
    def __init__(self):
        self.items = []
    def push(self, value):
        """Time: O(1) amortized. Auxiliary space: O(1)."""
        self.items.append(value)
    def pop(self):
        """Time: O(1). Auxiliary space: O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    def peek(self):
        """Time: O(1). Auxiliary space: O(1)."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    def is_empty(self):
        """Time: O(1). Auxiliary space: O(1)."""
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, value):
        """Time: O(1) amortized. Auxiliary space: O(1)."""
        self.items.append(value)
    def dequeue(self):
        """Time: O(n). Auxiliary space: O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    def front(self):
        """Time: O(1). Auxiliary space: O(1)."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    def is_empty(self):
        """Time: O(1). Auxiliary space: O(1)."""
        return len(self.items) == 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, value):
        """Time: O(1). Auxiliary space: O(1)."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def append(self, value):
        """Time: O(n). Auxiliary space: O(1)."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def search(self, value):
        """Time: O(n). Auxiliary space: O(1)."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    def delete(self, value):
        """Time: O(n). Auxiliary space: O(1)."""
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False
    def to_list(self):
        """Time: O(n). Auxiliary space: O(n) for the returned list."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack top:", stack.peek())
    print("Stack pop:", stack.pop())
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Queue front:", queue.front())
    print("Queue dequeue:", queue.dequeue())
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.prepend(5)
    print("Linked list:", linked_list.to_list())
    print("Found 20:", linked_list.search(20))
    linked_list.delete(20)
    print("After deleting 20:", linked_list.to_list())
