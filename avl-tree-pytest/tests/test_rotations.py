import avl

def test_left_rotation():
    root = avl.Node(10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)

    assert root.value == 20
    assert root.left.value == 10
    assert root.right.value == 30

    assert avl.height(root) == 2