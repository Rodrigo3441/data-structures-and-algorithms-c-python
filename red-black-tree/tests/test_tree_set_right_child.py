import tree

def test_set_right_child():
    rb_tree = tree.RedBlackTree()
    parent_node = tree.Node(20)
    child_node = tree.Node(30)

    rb_tree.set_right_child(parent_node, child_node)

    assert parent_node.right == child_node
    assert child_node.parent == parent_node

def test_set_right_child_with_none():
    rb_tree = tree.RedBlackTree()
    parent_node = tree.Node(20)

    rb_tree.set_right_child(parent_node, None)

    assert parent_node.right is None

def test_set_right_child_with_parent_none():
    rb_tree = tree.RedBlackTree()
    child_node = tree.Node(30)

    rb_tree.set_right_child(None, child_node)

    assert child_node.parent is None