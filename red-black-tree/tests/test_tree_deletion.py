import tree

def test_delete_nonexistent_node():
    rb_tree = tree.RedBlackTree()
    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)

    rb_tree.delete(99)

    assert rb_tree.root.value == 10
    assert rb_tree.root.left.value == 5
    assert rb_tree.root.right.value == 20

def test_delete_left_leaf():
    rb_tree = tree.RedBlackTree()
    rb_tree.insertion(10)
    rb_tree.insertion(5)

    rb_tree.delete(5)

    assert rb_tree.root.value == 10
    assert rb_tree.root.left is None
    assert rb_tree.root.right is None

def test_delete_right_leaf():
    rb_tree = tree.RedBlackTree()
    rb_tree.insertion(10)
    rb_tree.insertion(15)

    rb_tree.delete(15)

    assert rb_tree.root.value == 10
    assert rb_tree.root.left is None
    assert rb_tree.root.right is None

def test_delete_root_leaf():
    rb_tree = tree.RedBlackTree()
    rb_tree.insertion(10)

    rb_tree.delete(10)

    assert rb_tree.root is None

def test_delete_node_with_right_child():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_15 = tree.Node(15)
    node_20 = tree.Node(20)

    node_10.color = "B"
    node_15.color = "R"
    node_20.color = "R"

    rb_tree.root = node_10
    rb_tree.set_right_child(node_10, node_15)
    rb_tree.set_right_child(node_15, node_20)

    rb_tree.delete(15)

    assert rb_tree.root is node_10
    assert node_10.right is node_20
    assert node_20.parent is node_10
    assert node_10.left is None
    assert node_20.left is None
    assert node_20.right is None


def test_delete_node_with_left_child():
    rb_tree = tree.RedBlackTree()

    node_20 = tree.Node(20)
    node_15 = tree.Node(15)
    node_10 = tree.Node(10)

    node_20.color = "B"
    node_15.color = "R"
    node_10.color = "R"

    rb_tree.root = node_20
    rb_tree.set_left_child(node_20, node_15)
    rb_tree.set_left_child(node_15, node_10)

    rb_tree.delete(15)

    assert rb_tree.root is node_20
    assert node_20.left is node_10
    assert node_10.parent is node_20
    assert node_20.right is None
    assert node_10.left is None
    assert node_10.right is None


def test_delete_root_with_one_child():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_20 = tree.Node(20)

    node_10.color = "B"
    node_20.color = "R"

    rb_tree.root = node_10
    rb_tree.set_right_child(node_10, node_20)

    rb_tree.delete(10)

    assert rb_tree.root is node_20
    assert node_20.parent is None
    assert node_20.left is None
    assert node_20.right is None