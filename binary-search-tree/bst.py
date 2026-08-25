class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# insert a new value to the tree
def insert(root, key):
    if root is None:
        return Node(key)
    
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root

# search for a value in the tree and return the node address
def search(root: Node | None, target: int) -> Node | None:
    if root is None:
        return None

    if root.value == target:
        return root
    
    elif root.value < target:
        return search(root.right, target)
    
    else: 
        return search(root.left, target)

# return the lowest value in a tree
def find_min(root: Node | None) -> int | None:
    if root is None:
        return None

    if root.left is not None:
        return find_min(root.left)

    return root.value

# return the highest value in a tree
def find_max(root: Node | None) -> int | None:
    if root is None:
        return None

    if root.right is not None:
        return find_max(root.right)

    return root.value

# return the tree height for a generic tree
def find_height(root: Node | None) -> int:
    if root is None:
        return -1
    
    l_height = find_height(root.left)
    r_height = find_height(root.right)

    return max(l_height, r_height) + 1

# delete a node handling all the three cases:
# a leaf node, a node with one and two childs
def delete_node(root: Node | None, target: int) -> Node | None:
    if root is None:
        return None


    if target < root.value:
        root.left = delete_node(root.left, target)

    elif target > root.value:
        root.right = delete_node(root.right, target)

    else:
        # remove a leaf node from the tree
        if root.left is None and root.right is None:
            print(f'Deleted a leaf node: {root.value}')
            return None

        # remove a node with two child
        elif root.left is not None and root.right is not None:
            lowest_right = find_min(root.right)
            root.value = lowest_right
            right_subtree = delete_node(root.right, lowest_right)
            root.right = right_subtree



        # remove a node with one child
        else:
            if root.left is None:
                return root.right
            else:
                return root.left


    return root
    

# left | root | right
def inorder(root: Node | None):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# root | left | right
def preorder(root: Node | None):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

# print a tree following: left | right | root
def postorder(root: Node | None):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')


# print the tree in a nice way
def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)

        print("     " * level + str(root.value))

        print_tree(root.left, level + 1)