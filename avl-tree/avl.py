class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1



# return the tree height for a generic tree
def height(node) -> int:
    if node is None:
        return 0
    
    return node.height

# return the highest height for a node
def max_height(subtree1: Node, subtree2: Node) -> int:
    return 1 + max(height(subtree1), height(subtree2))

# return the lowest value within a tree
def return_min(root) -> int | None:
    if root is None:
        return None

    if root.left is not None:
        return return_min(root.left)
    
    return root.value

# return the highest valeu within a tree
def return_max(root) -> int | None:
    if root is None:
        return None

    if root.right is not None:
        return return_max(root.right)
    
    return root.value


# return the height difference between the left and the right subtree
def balance(node) -> int:
    if node is None:
        return 0
    return height(node.left) - height(node.right)


# search for a value within the tree
def search(node: Node, target: int) -> int | None:
    if node is None:
        return None

    if target == node.value:
        return target
    elif target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)


# insert a new value to the tree
def insert(root, value):
    if root is None:
        return Node(value)
    
    if root.value == value:
        return root
    if value < root.value:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    # root.height = 1 + max(height(root.right), height(root.left))
    root.height = 1 + max_height(root.right, root.left)
    balance_factor = balance(root)


    # right rotation
    if balance_factor > 1 and value < root.left.value:
        return right_rotation(root)

    # left rotation
    if balance_factor < -1 and value > root.right.value:
        return left_rotation(root)

    # left-right
    if balance_factor > 1 and value > root.left.value:
        root.left = left_rotation(root.left)
        return right_rotation(root)

    # right_left
    if balance_factor < -1 and value < root.right.value:
        root.right = right_rotation(root.right)
        return left_rotation(root)

    return root

def delete(root, target) -> Node | None:
    if root is None:
        return None

    if target < root.value:
        root.left = delete(root.left, target)

    elif target > root.value:
        root.right = delete(root.right, target) 

    else:
        # remove a leaf node
        if root.left is None and root.right is None:
            return None

        # remove a node with two childs
        elif root.left is not None and root.right is not None:
            lowest_right = return_min(root.right)
            root.value = lowest_right
            right_subtree = delete(root.right, lowest_right)
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

    root.height = 1 + max_height(root.right, root.left)
    balance_factor = balance(root)

    # right rotation
    if balance_factor > 1 and balance(root.left) >= 0:
        print('right rotation')
        return right_rotation(root)

    # left rotation
    if balance_factor < -1 and balance(root.right) <= 0:
        print('left rotation')
        return left_rotation(root)

    # left-right
    if balance_factor > 1 and balance(root.left) < 0:
        print('left-right rotation')
        root.left = left_rotation(root.left)
        return right_rotation(root)

    # right_left
    if balance_factor < -1 and balance(root.right) > 0:
        print('right-left rotation')
        root.right = right_rotation(root.right)
        return left_rotation(root)


    return root


# define the right rotation function
def right_rotation(root: Node):
    left_subtree = root.left
    left_right_subtree = left_subtree.right

    left_subtree.right = root
    left_subtree.right.left = left_right_subtree

    root = left_subtree

    root.right.height = max_height(root.right.right, root.right.left)
    root.height = max_height(root.left, root.right)

    return root

# define the left rotation function
def left_rotation(root: Node):
    right_subtree = root.right
    right_left_subtree = right_subtree.left

    right_subtree.left = root
    right_subtree.left.right = right_left_subtree

    root = right_subtree

    root.left.height = max_height(root.left.left, root.left.right)
    root.height = max_height(root.right, root.left)

    return root

# check the balance of the tree
def check_balance(root: Node):
    if root is None:
        return

    check_balance(root.left)
    print(height(root.left) - height(root.right))
    check_balance(root.right)