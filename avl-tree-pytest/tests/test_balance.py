import avl

def test_balance():
    root = avl.Node(10)
    assert avl.balance(root) == 0

    root = avl.insert(root, -10)
    assert avl.balance(root) == 1

    root1 = avl.Node(0)
    root1 = avl.insert(root1, 10)
    assert avl.balance(root1) == -1