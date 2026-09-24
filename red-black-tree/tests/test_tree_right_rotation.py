import tree

def test_rotate_right():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_20 = tree.Node(20)

    rb_tree.root = node_20
    rb_tree.set_left_child(node_20, node_10)

    rb_tree.rotate_right(node_20)

    assert rb_tree.root is node_10
    assert node_10.right is node_20
    assert node_20.parent is node_10

def test_rotate_right_non_root():
    rb_tree = tree.RedBlackTree()

    node_5 = tree.Node(5)
    node_10 = tree.Node(10)
    node_20 = tree.Node(20)

    rb_tree.root = node_5

    rb_tree.set_right_child(node_5, node_20)
    rb_tree.set_left_child(node_20, node_10)

    rb_tree.rotate_right(node_20)

    assert rb_tree.root is node_5
    assert node_5.right is node_10
    assert node_10.parent is node_5
    assert node_10.right is node_20
    assert node_20.parent is node_10

def test_rotate_right_with_middle_subtree():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_15 = tree.Node(15)
    node_20 = tree.Node(20)

    rb_tree.root = node_20

    rb_tree.set_left_child(node_20, node_10)
    rb_tree.set_right_child(node_10, node_15)

    rb_tree.rotate_right(node_20)

    assert rb_tree.root is node_10
    assert node_10.right is node_20
    assert node_20.parent is node_10
    assert node_20.left is node_15
    assert node_15.parent is node_20

def test_rotate_right_non_root_with_middle_subtree():
    rb_tree = tree.RedBlackTree()

    node_5 = tree.Node(5)
    node_10 = tree.Node(10)
    node_20 = tree.Node(20)
    node_15 = tree.Node(15)

    rb_tree.root = node_5

    rb_tree.set_right_child(node_5, node_20)
    rb_tree.set_left_child(node_20, node_10)
    rb_tree.set_right_child(node_10, node_15)

    rb_tree.rotate_right(node_20)

    assert rb_tree.root is node_5
    assert node_5.right is node_10
    assert node_10.parent is node_5
    assert node_10.right is node_20
    assert node_20.parent is node_10
    assert node_20.left is node_15
    assert node_15.parent is node_20