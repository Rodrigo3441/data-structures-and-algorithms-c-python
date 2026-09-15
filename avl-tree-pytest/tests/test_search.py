import avl

def test_search():
    root = None

    assert avl.search(root, 23) is None

    root = avl.insert(root, 10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 40)
    root = avl.insert(root, 33)

    assert avl.search(root, 10).value == 10
    assert avl.search(root, 44) is None
