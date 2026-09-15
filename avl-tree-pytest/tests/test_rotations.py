import avl

def test_left_rotation():
    root = avl.Node(10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)

    assert root.value == 20
    assert root.left.value == 10
    assert root.right.value == 30

    assert avl.height(root) == 2

def test_right_rotation():
    root = avl.Node(30)
    root = avl.insert(root, 20)
    root = avl.insert(root, 10)

    assert root.value == 20
    assert root.left.value == 10
    assert root.right.value == 30

def test_left_right_rotation():
    root = avl.Node(30)
    root = avl.insert(root, 10)
    root = avl.insert(root, 20)

    assert root.value == 20
    assert root.left.value == 10
    assert root.right.value == 30

def test_right_left_rotation():
    root = avl.Node(10)
    root = avl.insert(root, 30)
    root = avl.insert(root, 20)

    assert root.value == 20
    assert root.left.value == 10
    assert root.right.value == 30