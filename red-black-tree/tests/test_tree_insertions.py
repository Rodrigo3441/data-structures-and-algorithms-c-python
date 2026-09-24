import tree

def test_insertion_empty_tree():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)

    assert rb_tree.root is not None
    assert rb_tree.root.value == 10
    assert rb_tree.root.parent is None

def test_insertion_duplicate_root():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    original_root = rb_tree.root

    rb_tree.insertion(10)

    assert rb_tree.root is original_root
    assert rb_tree.root.value == 10

def test_insertion_left_of_root():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)

    assert rb_tree.root.left is not None
    assert rb_tree.root.left.value == 5
    assert rb_tree.root.left.parent is rb_tree.root

def test_insertion_builds_bst():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)
    rb_tree.insertion(15)
    rb_tree.insertion(30)

    assert rb_tree.root.value == 10

    assert rb_tree.root.left.value == 5
    assert rb_tree.root.left.parent is rb_tree.root

    assert rb_tree.root.right.value == 20
    assert rb_tree.root.right.parent is rb_tree.root

    assert rb_tree.root.right.left.value == 15
    assert rb_tree.root.right.left.parent is rb_tree.root.right

    assert rb_tree.root.right.right.value == 30
    assert rb_tree.root.right.right.parent is rb_tree.root.right

def test_insertion_ignores_duplicate():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)
    rb_tree.insertion(15)

    original_node = rb_tree.root.right.left

    rb_tree.insertion(15)

    assert rb_tree.root.right.left is original_node
    assert rb_tree.root.right.left.left is None
    assert rb_tree.root.right.left.right is None

def test_first_insertion_is_black():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)

    assert rb_tree.root.value == 10
    assert rb_tree.root.color == 'B'

def test_insertion_creates_red_non_root_node():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)

    assert rb_tree.root.color == 'B'
    assert rb_tree.root.left.color == 'R'
    assert rb_tree.root.right.color == 'R'
