class Node:
    """Class describing a binary tree node"""
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    """Class describing a binary tree"""
    def __init__(self):
        self.root = None

    def __find_node(self, node, parent, data):
        if node is None:
            return None, parent, False
        elif node.data == data:
            return node, parent, False
        elif data < node.data:
            if node.left:
                return self.__find_node(node.left, node, data)
        elif data > node.data:
            if node.right:
                return self.__find_node(node.right, node, data)

        return node, parent, True

    def append(self, data):
        if self.root is None:
            self.root = Node(data)
            return data

        node, parent, flag = self.__find_node(self.root, None, data)
        if flag and node:
            if data < node.data:
                node.left = Node(data)
            else:
                node.right = Node(data)

        return data

    def __pop_leaf(self, node, parent):
        if parent.left is node:
            parent.left = None
        elif parent.right is None:
            parent.right = None

    def __pop_one_child(self, node, parent):
        if parent.left is node:
            if node.left:
                parent.left = node.left
                node.left = None
            else:
                parent.left = node.right
                node.right = Node
        elif parent.right is node:
            if node.left:
                parent.right = node.left
                node.left = None
            else:
                parent.right = node.right
                node.right = Node

    def find_min_node(self, node, parent):
        if node.left is None:
            return node, parent
        return self.find_min_node(node.left, node)

    def pop(self, data):
        node, parent, flag = self.__find_node(self.root, None, data)
        if flag:
            return None
        if node.left is None and node.right is None:
            self.__pop_leaf(node, parent)
        elif node.left is None or node.right is None:
            self.__pop_one_child(node, parent)
        else:
            min_node, parent = self.find_min_node(node.right, node)
            node.data = min_node.data
            self.__pop_one_child(min_node, parent)

    def print_tree(self, node):
        if node is None:
            return
        # self.print_tree(node.left)
        # print(node.data, end=" ")
        # self.print_tree(node.right)
        p = self.root
        v = [p]

        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn


binary_tree = BinaryTree()
binary_tree.append(10)
binary_tree.append(4)
binary_tree.append(7)
binary_tree.append(2)
binary_tree.append(3)
binary_tree.append(5)
binary_tree.append(4)
binary_tree.append(2)

binary_tree.print_tree(binary_tree.root)