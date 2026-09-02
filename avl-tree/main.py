import avl
import avl_class

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




if __name__ == '__main__':
    # root = avl.Node(12)
    # root = avl.insert(root, 11)
    # root = avl.insert(root, 10)
    # root = avl.insert(root, 9)
    # root = avl.insert(root, 8)
    # root = avl.insert(root, 7)

    root = avl.Node(50)

    root = avl.insert(root, 30)
    root = avl.insert(root, 70)
    root = avl.insert(root, 20)
    root = avl.insert(root, 40)
    root = avl.insert(root, 60)
    root = avl.insert(root, 80)
    root = avl.insert(root, 10)
    root = avl.insert(root, 25)
    root = avl.insert(root, 35)
    root = avl.insert(root, 45)
    root = avl.insert(root, 55)
    root = avl.insert(root, 65)
    root = avl.insert(root, 75)
    root = avl.insert(root, 90)
    root = avl.insert(root, 5)
    root = avl.insert(root, 15)
    root = avl.insert(root, 27)
    root = avl.insert(root, 26)
    root = avl.insert(root, 28)

    print('subtree before deletion:\n')
    
    print_tree(root)

    # avl.delete(root, 90)
    # avl.delete(root, 65)
    # avl.delete(root, 40)
    # avl.delete(root, 70)
    # avl.delete(root, 70)
    avl.delete(root, 30)
    root = avl.delete(root, 50)
    root = avl.delete(root, 70)

    print('\n\nsubtree after deletion:')

    print_tree(root)


    print('AVL Class implementation:')
    tree = avl_class.AVLTree()

    tree.insert(50)