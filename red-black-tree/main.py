from tree import RedBlackTree

def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    if node.right is not None:
        print_tree(
            node.right,
            prefix + ("│   " if is_left else "    "),
            False
        )

    print(
        prefix +
        ("└── " if is_left else "┌── ") +
        f"{node.value} ({node.color})"
    )

    if node.left is not None:
        print_tree(
            node.left,
            prefix + ("    " if is_left else "│   "),
            True
        )

rb_tree = RedBlackTree()

rb_tree.insertion(10)
rb_tree.insertion(5)
rb_tree.insertion(20)
rb_tree.insertion(3)
rb_tree.insertion(6)
rb_tree.insertion(15)
rb_tree.insertion(25)
rb_tree.insertion(8)



print_tree(rb_tree.root)