import tree

def test_insertion_fixup_root_is_black():
    rb_tree = tree.RedBlackTree()

    node = tree.Node(10)
    node.color = "R"
    rb_tree.root = node

    rb_tree.insertion_fixup(node)

    assert node.color == "B"

def test_insertion_fixup_red_parent_and_uncle():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_5 = tree.Node(5)
    node_20 = tree.Node(20)
    node_1 = tree.Node(1)

    node_10.color = "B"

    rb_tree.root = node_10
    rb_tree.set_left_child(node_10, node_5)
    rb_tree.set_right_child(node_10, node_20)
    rb_tree.set_left_child(node_5, node_1)

    rb_tree.insertion_fixup(node_1)

    assert node_5.color == "B"
    assert node_20.color == "B"
    assert node_10.color == "B"
    assert node_1.color == "R"

def test_insertion_fixup_black_uncle_does_not_crash():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_5 = tree.Node(5)
    node_1 = tree.Node(1)

    node_10.color = "B"
    node_5.color = "R"
    node_1.color = "R"

    rb_tree.root = node_10
    rb_tree.set_left_child(node_10, node_5)
    rb_tree.set_left_child(node_5, node_1)

    rb_tree.insertion_fixup(node_1)

def test_insertion_fixup_ll_case():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_5 = tree.Node(5)
    node_1 = tree.Node(1)

    node_10.color = "B"
    node_5.color = "R"
    node_1.color = "R"

    rb_tree.root = node_10
    rb_tree.set_left_child(node_10, node_5)
    rb_tree.set_left_child(node_5, node_1)

    rb_tree.insertion_fixup(node_1)

    assert rb_tree.root is node_5
    assert node_5.color == "B"
    assert node_1.color == "R"
    assert node_10.color == "R"

    assert node_5.left is node_1
    assert node_5.right is node_10
    assert node_1.parent is node_5
    assert node_10.parent is node_5

def test_insertion_fixup_rr_case():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_20 = tree.Node(20)
    node_30 = tree.Node(30)

    node_10.color = "B"
    node_20.color = "R"
    node_30.color = "R"

    rb_tree.root = node_10
    rb_tree.set_right_child(node_10, node_20)
    rb_tree.set_right_child(node_20, node_30)

    rb_tree.insertion_fixup(node_30)

    assert rb_tree.root is node_20
    assert node_20.color == "B"
    assert node_10.color == "R"
    assert node_30.color == "R"

    assert node_20.left is node_10
    assert node_20.right is node_30
    assert node_10.parent is node_20
    assert node_30.parent is node_20

def test_insertion_fixup_lr_case():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_5 = tree.Node(5)
    node_7 = tree.Node(7)

    node_10.color = "B"
    node_5.color = "R"
    node_7.color = "R"

    rb_tree.root = node_10
    rb_tree.set_left_child(node_10, node_5)
    rb_tree.set_right_child(node_5, node_7)

    rb_tree.insertion_fixup(node_7)

    print(rb_tree.root.value)
    assert rb_tree.root is node_7
    assert node_7.color == "B"
    assert node_5.color == "R"
    assert node_10.color == "R"

    assert node_7.left is node_5
    assert node_7.right is node_10
    assert node_5.parent is node_7
    assert node_10.parent is node_7

def test_insertion_fixup_rl_case():
    rb_tree = tree.RedBlackTree()

    node_10 = tree.Node(10)
    node_20 = tree.Node(20)
    node_15 = tree.Node(15)

    node_10.color = "B"
    node_20.color = "R"
    node_15.color = "R"

    rb_tree.root = node_10
    rb_tree.set_right_child(node_10, node_20)
    rb_tree.set_left_child(node_20, node_15)

    rb_tree.insertion_fixup(node_15)

    assert rb_tree.root is node_15
    assert node_15.color == "B"
    assert node_10.color == "R"
    assert node_20.color == "R"

    assert node_15.left is node_10
    assert node_15.right is node_20
    assert node_10.parent is node_15
    assert node_20.parent is node_15

def test_insertion_balances_ll_case():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(1)

    assert rb_tree.root.value == 5
    assert rb_tree.root.color == "B"

    assert rb_tree.root.left.value == 1
    assert rb_tree.root.left.color == "R"

    assert rb_tree.root.right.value == 10
    assert rb_tree.root.right.color == "R"

def test_insertion_balances_multiple_nodes():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)
    rb_tree.insertion(1)
    rb_tree.insertion(7)
    rb_tree.insertion(15)
    rb_tree.insertion(30)

    assert rb_tree.root is not None
    assert rb_tree.root.color == "B"

    # Every parent-child relationship should not be red-red
    def check_no_red_red(node):
        if node is None:
            return

        if node.color == "R":
            assert node.left is None or node.left.color == "B"
            assert node.right is None or node.right.color == "B"

        check_no_red_red(node.left)
        check_no_red_red(node.right)

    check_no_red_red(rb_tree.root)

def black_height(node):
    if node is None:
        return 1

    left_height = black_height(node.left)
    right_height = black_height(node.right)

    assert left_height == right_height

    return left_height + (1 if node.color == "B" else 0)

def test_insertion_preserves_black_height():
    rb_tree = tree.RedBlackTree()

    values = [10, 5, 20, 1, 7, 15, 30, 0, 3, 6, 8]

    for value in values:
        rb_tree.insertion(value)

    assert rb_tree.root.color == "B"

    black_height(rb_tree.root)