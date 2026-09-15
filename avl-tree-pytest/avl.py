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

def return_max(node: Node) -> Node | None:
    if node is None:
        return None

    if node.right is not None:
        return return_max(node.right)

    return node

def search(node: Node, target: int) -> Node | None:
    if node is None:
        return None

    if target == node.value:
        return node
    elif target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)
    

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
        return right_rotation(node)

    # left rotation
    if balance_factor < 1 and value > node.right.value:
        print('left rotation')
        return left_rotation(node)

    # left-right rotation
    if balance_factor > 1 and value > node.left.value:
        print('left-right rotation')
        node.left = left_rotation(node.left)
        return right_rotation(node)

    # right-left rotation
    if balance_factor < 1 and value < node.right.value:
        print('right-left rotation')
        node.right = right_rotation(node.right)
        return left_rotation(node)

    return node

def left_rotation(node: Node) -> Node:
    low_right = return_min(node.right) #20
    low_right.left = node #20.left -> 10
    node.right = None #10.right -> none

    low_right.left.height = max_height(low_right.left.left, low_right.left.right) #new height for 10
    low_right.height = max_height(low_right.left, low_right.right) #new height for 20
    
    return low_right


def right_rotation(node:Node) -> Node:
    high_left = return_max(node.left) #20
    high_left.right = node #20.right -> 30
    node.left = None #30.left -> none

    high_left.right.height = max_height(high_left.right.right, high_left.right.left) #new height for 30 
    high_left.height = max_height(high_left.left, high_left.right) #new height for 20

    return high_left

def delete(node: Node, target: int) -> Node | None:
    if node is None:
        return None

    if target < node.value:
        node.left = delete(node.left, target)
    elif target > node.value:
        node.right = delete(node.right, target)
    else:
        # remove a leaf node
        if node.left is None and node.right is None:
            return None

        # remove a node with two childs
        elif node.left is not None and node.right is not None:
            lowest_right = return_min(node.right)
            node.value = lowest_right.value
            right_subtree = delete(node.right, lowest_right.value)
            node.right = right_subtree
            return node

        # remove a node with only one child
        else:
            if node.left is None:
                return node.right
            else:
                return node.left

    if node is None:
        return None

    node.height = max_height(node.left, node.right)
    balance_factor = balance(node)

    # right rotation
    if balance_factor > 1 and balance(node.left) >= 0:
        print('right rotation')
        return right_rotation(node)

    # left rotation
    if balance_factor < 1 and balance(node.right) <= 0:
        print('left rotation')
        return left_rotation(node)

    # left-right rotation
    if balance_factor > 1 and balance(node.left) < 0:
        print('left-right rotation')
        node.left = left_rotation(node.left)
        return right_rotation(node)

    # right-left rotation
    if balance_factor < 1 and balance(node.right) > 0:
        print('right-left rotation')
        node.right = right_rotation(node.right)
        return left_rotation(node)

    return node

def print_inorder(node: Node) -> None:
    if node is not None:
        print_inorder(node.left)
        print(node.value, end=' ')
        print_inorder(node.right)

def print_preorder(node: Node) -> None:
    if node is not None:
        print(node.value, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)

def print_postorder(node: Node) -> None:
    if node is not None:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.value, end=' ')
