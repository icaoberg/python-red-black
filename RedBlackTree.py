from Node import Node, RED, BLACK
import random

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, BLACK)
        self.root = self.NIL
        self.number_of_nodes = 0

    def random(self, number_of_nodes):
        self.NIL = Node(None, BLACK)
        self.root = self.NIL
        self.number_of_nodes = 0

        if number_of_nodes <= 0:
            return

        elements = random.sample(range(number_of_nodes), number_of_nodes)
        for e in elements:
            self.insert(e)

    def get_root(self):
        return self.root if self.root is not self.NIL else None

    def insert(self, element):
        node = Node(element, RED)
        node.left = self.NIL
        node.right = self.NIL
        node.parent = None

        parent = None
        current = self.root

        while current is not self.NIL:
            parent = current
            if node.get() < current.get():
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.get() < parent.get():
            parent.left = node
        else:
            parent.right = node

        self.number_of_nodes += 1
        self.__fix_insert(node)

    def __fix_insert(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.__rotate_left(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.__rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.__rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.__rotate_left(node.parent.parent)

        self.root.color = BLACK

    def __rotate_left(self, x):
        y = x.right
        x.right = y.left

        if y.left is not self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def __rotate_right(self, x):
        y = x.left
        x.left = y.right

        if y.right is not self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def is_empty(self):
        return self.number_of_nodes == 0

    def size(self):
        return self.number_of_nodes

    def min(self):
        if self.is_empty():
            return None
        return self.__min(self.root).get()

    def __min(self, node):
        while node.left is not self.NIL:
            node = node.left
        return node

    def max(self):
        if self.is_empty():
            return None
        return self.__max(self.root).get()

    def __max(self, node):
        while node.right is not self.NIL:
            node = node.right
        return node

    def inorder(self):
        result = []
        if not self.is_empty():
            self.__inorder(self.root, result)
        return result

    def __inorder(self, node, result):
        if node is self.NIL:
            return
        self.__inorder(node.left, result)
        result.append(node.get())
        self.__inorder(node.right, result)

    def search(self, element):
        node = self.root
        while node is not self.NIL:
            if element == node.get():
                return node
            elif element < node.get():
                node = node.left
            else:
                node = node.right
        return None

    def __len__(self):
        return self.number_of_nodes

    def __repr__(self):
        return f"RedBlackTree(size={self.number_of_nodes}, inorder={self.inorder()})"
