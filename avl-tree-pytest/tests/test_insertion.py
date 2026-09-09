import avl

def test_insertion():
    root = 15
    left = 10
    right = 20

    node = avl.Node(root)
    node = avl.insert(node, left)
    node = avl.insert(node, right)
    assert node.left.value == left
    assert node.right.value == right