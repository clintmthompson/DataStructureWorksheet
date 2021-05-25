
from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_to_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def contains(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                print("True")
                return True
            node = node.next
        print("False")
        return False
