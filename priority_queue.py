class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Priority_Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True

        return False

    def enqueue(self, data):
        new_node = Node(data)
        comp = self.head
        pre = Node()

        if self.is_empty():
            self.head = new_node
            return

        if new_node.data < comp.data:
            self.head = new_node
            new_node.next = comp
        else:
            while True:
                if comp.data >= new_node.data:
                    pre.next = new_node
                    new_node.next = comp
                    break
                elif comp.data < new_node.data:
                    if comp.next is None:
                        comp.next = new_node
                        break
                    else:
                        pre = comp
                        comp = comp.next

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
