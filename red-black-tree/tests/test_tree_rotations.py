import tree

def test_rotate_left():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_20 = tree.Node(20)

    rb_tree.root = node_10
    rb_tree.set_right_child(node_10, node_20)

    rb_tree.rotate_left(node_10)

    assert rb_tree.root is node_20
    assert node_20.left is node_10
    assert node_10.parent is node_20