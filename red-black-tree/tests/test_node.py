import tree

def test_node_initialization():
    node = tree.Node(10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None
    assert node.color == 'R'
    assert node.parent is None