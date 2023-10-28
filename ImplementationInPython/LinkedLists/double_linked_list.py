class Node:
    """Class describing an element of double linked list"""
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    """Class describing double linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self) -> int:
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
        node.prev = self.tail
        self.tail = node

    def push_front(self, data: int):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def pop_back(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return
        node = self.tail.prev
        self.tail.prev, node.next = None, None
        self.tail = node

    def pop_front(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return
        node = self.head.next
        self.head.next = None
        node.prev = None
        self.head = node

    def insert(self, index: int, data: int):
        if self.head is None:
            return
        elif index == 0:
            self.push_front(data)
            return
        elif index >= self.length():
            self.push_back(data)
            return
        elif index < 0:
            self.insert(self.length() + index, data)
            return
        node: Node = Node(data)
        left: Node = self.head
        for i in range(index-1):
            left = left.next
        right: Node = left.next
        left.next = node
        node.next = right
        node.prev = left
        right.prev = node

    def erase(self, index: int):
        if self.head is None:
            return
        elif index == 0:
            self.pop_front()
            return
        elif index >= self.length() - 1:
            self.pop_back()
            return
        elif index < 0:
            self.erase(self.length() + index)
            return
        left: Node = self.head
        for i in range(index - 1):
            left = left.next
        right: Node = left.next.next
        left.next.prev = None
        left.next.next = None
        left.next = right
        right.prev = left

    def print_list(self, reverse=False):
        if reverse:
            node = self.tail
            while node is not None:
                print(node.data, end='->')
                node = node.prev
            print('None')
            return
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print('None')


double_linked_list = DoubleLinkedList()
double_linked_list.push_back(1)
double_linked_list.push_back(2)
double_linked_list.push_back(3)
double_linked_list.push_back(4)
double_linked_list.erase(-2)
double_linked_list.print_list()

