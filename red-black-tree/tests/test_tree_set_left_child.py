import tree

def test_set_left_child():
    rb_tree = tree.RedBlackTree()
    parent_node = tree.Node(20)
    child_node = tree.Node(10)

    rb_tree.set_left_child(parent_node, child_node)

    assert parent_node.left == child_node
    assert child_node.parent == parent_node

def test_set_left_child_with_none():
    rb_tree = tree.RedBlackTree()
    parent_node = tree.Node(20)

    rb_tree.set_left_child(parent_node, None)

    assert parent_node.left is None

def test_set_left_child_with_parent_none():
    rb_tree = tree.RedBlackTree()
    child_node = tree.Node(10)

    rb_tree.set_left_child(None, child_node)

    assert child_node.parent is None