import avl

# left | root | right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# print the tree in a nice way
def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)

        print("     " * level + str(root.value))

        print_tree(root.left, level + 1)

tree = avl.AVLTree()


if __name__ == '__main__':

    tree.root = tree.insert(tree.root, 10)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 30)
    tree.root = tree.insert(tree.root, 40)
    tree.root = tree.insert(tree.root, 50)

    print_tree(tree.root)