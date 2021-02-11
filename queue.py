class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None    # head를 가리키는 포인터
        self.tail = None    # tail을 가리키는 포인터

    def is_empty(self):
        if not self.head:
            return True

        return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data
