import tree

def test_tree_initialization():
    rb_tree = tree.RedBlackTree()
    assert rb_tree.root is None

def test_get_root():
    rb_tree = tree.RedBlackTree()

    assert rb_tree.root is None

    node = tree.Node(10)
    rb_tree.root = node

    assert rb_tree.root == node

def test_is_left_child():
    rb_tree = tree.RedBlackTree()

    parent_node = tree.Node(20)
    left_child_node = tree.Node(10)
    right_child_node = tree.Node(30)

    rb_tree.set_left_child(parent_node, left_child_node)
    rb_tree.set_right_child(parent_node, right_child_node)

    assert rb_tree.is_left_child(left_child_node) is True
    assert rb_tree.is_left_child(right_child_node) is False
    assert rb_tree.is_left_child(parent_node) is False

def test_is_right_child():
    rb_tree = tree.RedBlackTree()

    parent_node = tree.Node(20)
    left_child_node = tree.Node(10)
    right_child_node = tree.Node(30)

    rb_tree.set_left_child(parent_node, left_child_node)
    rb_tree.set_right_child(parent_node, right_child_node)

    assert rb_tree.is_right_child(right_child_node) is True
    assert rb_tree.is_right_child(left_child_node) is False
    assert rb_tree.is_right_child(parent_node) is False