import tree

def test_search_single_node():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)

    result = rb_tree.search(10)

    assert result is rb_tree.root
    assert result.value == 10

def test_search_existing_nodes():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)
    rb_tree.insertion(1)
    rb_tree.insertion(7)
    rb_tree.insertion(15)
    rb_tree.insertion(30)

    assert rb_tree.search(10).value == 10
    assert rb_tree.search(5).value == 5
    assert rb_tree.search(20).value == 20
    assert rb_tree.search(1).value == 1
    assert rb_tree.search(7).value == 7
    assert rb_tree.search(15).value == 15
    assert rb_tree.search(30).value == 30

def test_search_nonexistent_value():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)

    assert rb_tree.search(999) is None
    assert rb_tree.search(6) is None
    assert rb_tree.search(-10) is None

def test_search_after_duplicate_insertion():
    rb_tree = tree.RedBlackTree()

    rb_tree.insertion(10)
    rb_tree.insertion(5)
    rb_tree.insertion(20)

    original_node = rb_tree.search(5)

    rb_tree.insertion(5)

    assert rb_tree.search(5) is original_node