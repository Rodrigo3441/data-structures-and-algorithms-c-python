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

    # return the highest height for a node
    def max_height(self, subtree1: Node, subtree2: Node) -> int:
        return 1 + max(self.height(subtree1), self.height(subtree2))

    # return the lowest value within a tree
    def return_min(self, root) -> int | None:
        if root is None:
            return None

        if root.left is not None:
            return self.return_min(root.left)
        
        return root.value

    # return the highest valeu within a tree
    def return_max(self, root) -> int | None:
        if root is None:
            return None

        if root.right is not None:
            return self.return_max(root.right)
        
        return root.value


    # return the height difference between the left and the right subtree
    def balance(self, node) -> int:
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)


    # search for a value within the tree
    def search(self, node: Node, target: int) -> int | None:
        if node is None:
            return None

        if target == node.value:
            return target
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)


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

        # root.height = 1 + max(height(root.right), height(root.left))
        root.height = 1 + self.max_height(root.right, root.left)
        balance_factor = self.balance(root)


        # right rotation
        if balance_factor > 1 and value < root.left.value:
            return self.right_rotation(root)

        # left rotation
        if balance_factor < -1 and value > root.right.value:
            return self.left_rotation(root)

        # left-right
        if balance_factor > 1 and value > root.left.value:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # right_left
        if balance_factor < -1 and value < root.right.value:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)

        return root

    def delete(self, root, target) -> Node | None:
        if root is None:
            return None

        if target < root.value:
            root.left = self.delete(root.left, target)

        elif target > root.value:
            root.right = self.delete(root.right, target) 

        else:
            # remove a leaf node
            if root.left is None and root.right is None:
                return None

            # remove a node with two childs
            elif root.left is not None and root.right is not None:
                lowest_right = self.return_min(root.right)
                root.value = lowest_right
                right_subtree = self.delete(root.right, lowest_right)
                root.right = right_subtree
                return root

            # remove a node with only one child
            else:
                if root.left is None:
                    return root.right
                else:
                    return root.left

        if root is None:
            return None

        root.height = 1 + self.max_height(root.right, root.left)
        balance_factor = self.balance(root)

        # right rotation
        if balance_factor > 1 and self.balance(root.left) >= 0:
            print('right rotation')
            return self.right_rotation(root)

        # left rotation
        if balance_factor < -1 and self.balance(root.right) <= 0:
            print('left rotation')
            return self.left_rotation(root)

        # left-right
        if balance_factor > 1 and self.balance(root.left) < 0:
            print('left-right rotation')
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)

        # right_left
        if balance_factor < -1 and self.balance(root.right) > 0:
            print('right-left rotation')
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)


        return root


    # define the right rotation function
    def right_rotation(self, root: Node):
        left_subtree = root.left
        left_right_subtree = left_subtree.right

        left_subtree.right = root
        left_subtree.right.left = left_right_subtree

        root = left_subtree

        root.right.height = self.max_height(root.right.right, root.right.left)
        root.height = self.max_height(root.left, root.right)

        return root

    # define the left rotation function
    def left_rotation(self, root: Node):
        right_subtree = root.right
        right_left_subtree = right_subtree.left

        right_subtree.left = root
        right_subtree.left.right = right_left_subtree

        root = right_subtree

        root.left.height = self.max_height(root.left.left, root.left.right)
        root.height = self.max_height(root.right, root.left)

        return root

    # check the balance of the tree
    def check_balance(self, root: Node):
        if root is None:
            return

        self.check_balance(root.left)
        print(self.balance(root))
        self.check_balance(root.right)