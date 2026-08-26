class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    # return the tree height for a generic tree
    def height(self, node) -> int:
        if node is None:
            return 0
        
        return node.height

    # return the height difference between the left and the right subtree
    def balance(self, node) -> int:
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # insert a new value to the tree
    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        if root.value == value:
            return root
        if value < root.value:
            root.left = self.insert(root.left, value)

        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.right), self.height(root.left))
        balance_factor = self.balance(root)

        # next: implement the rotation functions and the flags

        return root