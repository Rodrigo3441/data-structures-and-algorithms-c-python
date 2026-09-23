from platform import node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = 'R'  # New nodes are red by default
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, node):
        self.__root = node  

    def set_left_child(self, parent, child):
        if parent is None:
            return

        parent.left = child
        if child is not None:
            child.parent = parent

    def set_right_child(self, parent, child):
        if parent is None:
            return

        parent.right = child
        if child is not None:
            child.parent = parent

    def is_left_child(self, node):
        if node is None or node.parent is None:
            return False
        
        return node.parent.left is node

    def is_right_child(self, node):
        if node is None or node.parent is None:
            return False
        
        return node.parent.right is node

    def rotate_left(self, node: Node):
        pass
