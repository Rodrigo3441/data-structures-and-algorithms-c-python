import avl

def test_min():
    root = avl.Node(10)
    root = avl.insert(root, 0)
    root = avl.insert(root, -10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)

    assert avl.return_min(root).value == -10