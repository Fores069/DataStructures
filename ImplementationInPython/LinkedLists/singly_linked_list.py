class Node:
    """Class describing an element of singly linked list"""
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Class describing a singly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def push_back(self, data: int):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def push_front(self, data: int):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head = node

    def pop_back(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None
        self.tail = node

    def pop_front(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return
        self.head.next, self.head = None, self.head.next

    def print_list(self):
        if self.head is None:
            return
        node = self.head
        while node.next is not None:
            print(node.data, end='->')
            node = node.next
        print(node.data, end='->None')

    def insert(self, index: int, data: int):
        if self.head is None:
            return
        elif index == 0:
            self.push_front(data)
            return
        elif index >= self.length():
            self.push_back(data)
            return
        node = Node(data)
        left = self.head
        for i in range(index-1):
            left = left.next
        right = left.next
        left.next = node
        node.next = right
        print(left.data, right.data)

    def erase(self, index):
        if self.head is None:
            return
        elif index == 0:
            self.pop_front()
            return
        elif index >= self.length() - 1:
            self.pop_back()
            return
        left = self.head
        for i in range(index-1):
            left = left.next
        right = left.next.next
        left.next.next = None
        left.next = right


singly_linked_list = SinglyLinkedList()
singly_linked_list.push_back(1)
singly_linked_list.push_back(2)
singly_linked_list.push_front(0)
singly_linked_list.erase(1)
singly_linked_list.print_list()
