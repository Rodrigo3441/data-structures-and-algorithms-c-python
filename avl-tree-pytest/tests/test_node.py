import avl

def test_node():
    x = 10

    node = avl.Node(x)
    assert node.height == 1
    assert node.left is None
    assert node.right is None
    assert node.value == x


