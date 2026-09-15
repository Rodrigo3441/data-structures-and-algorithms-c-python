import avl

def test_deletion():
    root = avl.Node(10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)

    root = avl.delete(root, 20)

    assert root.value == 30
    assert root.left.value == 10
    assert root.right is None

    root = avl.delete(root, 30)

    assert root.value == 10
    assert root.right is None
    assert root.left is None

    root = avl.delete(root, 10)
    assert root is None