import avl

def test_height():
    root = avl.Node(20)
    assert root.height == avl.height(root)

def test_max_height():
    root = avl.Node(0) #height 1
    root = avl.insert(root, 10) #height 2
    root = avl.insert(root, 20) #height 3
    root = avl.insert(root, -10) #height still 3
    assert avl.max_height(root.left, root.right) == 3

    root2 = avl.Node(0)
    root2 = avl.Node(10)
    root2 = avl.Node(-10)
    assert avl.max_height(root2.left, root2.right) == 1