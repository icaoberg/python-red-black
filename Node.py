RED = 'RED'
BLACK = 'BLACK'

class Node:
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def is_leaf(self):
        return not self.has_left() and not self.has_right()

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def is_red(self):
        return self.color == RED

    def is_black(self):
        return self.color == BLACK

    def __repr__(self):
        return f"Node({self.value}, {self.color})"
