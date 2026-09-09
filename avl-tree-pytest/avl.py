class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def height(node: Node) -> int:
    if node is None:
        return 0

    return node.height

def max_height(subtree1: Node, subtree2: Node) -> int:
    return 1 + max(height(subtree1), height(subtree2))


def balance(node: Node) -> int:
    return height(node.left) - height(node.right)


def return_min(node: Node) -> Node | None:
    if node is None:
        return None

    if node.left is not None:
        return return_min(node.left)

    return node

def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    # find where to insert the new value
    if value == node.value:
        return node
    elif value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    # calculates the balance factor
    node.height = max_height(node.left, node.right)
    balance_factor = balance(node)

    # right rotation
    if balance_factor > 1 and value < node.left.value:
        print('right rotation')

    # left rotation
    if balance_factor < 1 and value > node.right.value:
        print('left rotation')
        return left_rotation(node)

    # left-right rotation
    if balance_factor > 1 and value > node.left.value:
        print('left-right rotation')

    # right-left rotation
    if balance_factor < 1 and value < node.right.value:
        print('right-left rotation')

    return node

def left_rotation(node: Node) -> Node:
    low_right = return_min(node.right)
    low_right.left = node
    node.right = None

    low_right.left.height = max_height(low_right.left.left, low_right.left.right)
    low_right.height = max_height(low_right.left, low_right.right)
    
    return low_right