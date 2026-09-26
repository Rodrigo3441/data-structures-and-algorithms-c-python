from platform import node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = 'R'  # New nodes are red by default
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, node):
        self.__root = node  

    def set_left_child(self, parent, child):
        if parent is None:
            return

        parent.left = child
        if child is not None:
            child.parent = parent

    def set_right_child(self, parent, child):
        if parent is None:
            return

        parent.right = child
        if child is not None:
            child.parent = parent

    def is_left_child(self, node):
        if node is None or node.parent is None:
            return False
        
        return node.parent.left is node

    def is_right_child(self, node):
        if node is None or node.parent is None:
            return False
        
        return node.parent.right is node

    def rotate_left(self, node: Node):
        new_top = node.right

        if node.parent is not None:
            if self.is_left_child(node):
                node.parent.left = new_top
            else:
                node.parent.right = new_top
            new_top.parent = node.parent
        else:
            self.root = new_top

        middle_subtree = new_top.left
        new_top.left = node
        node.right = middle_subtree

        if middle_subtree is not None:
            middle_subtree.parent = node

        node.parent = new_top

    def rotate_right(self, node: Node):
        new_top = node.left

        if node.parent is not None:
            if self.is_right_child(node):
                node.parent.right = new_top
            else:
                node.parent.left = new_top
            new_top.parent = node.parent
        else:
            self.root = new_top

        middle_subtree = new_top.right
        new_top.right = node
        node.left = middle_subtree

        if middle_subtree is not None:
            middle_subtree.parent = node

        node.parent = new_top

    def insertion(self, value: int):
        if self.root is None:
            self.root = Node(value)
            self.root.color = "B"
            return
            
        current = self.root
        new_node = Node(value)

        while current is not None:
            if value == current.value:
                return
            
            elif value < current.value:
                if current.left is None: # case when left pointer has no subtree
                    self.set_left_child(current, new_node)
                    self.insertion_fixup(new_node)
                    break
                else: # case when left has a subtree
                    
                    current = current.left
            else:
                if current.right is None: # case when right pointer has no subtree
                    self.set_right_child(current, new_node)
                    self.insertion_fixup(new_node)
                    break
                else: # case when right has a subtree
                    current = current.right


    def insertion_fixup(self, node: Node):
        if node.parent is None:
            node.color = "B"
            return 
        
        if node.parent.color == "B":
            return

        grandparent = node.parent.parent

        if self.is_left_child(node.parent):
            uncle = grandparent.right
        else:
            uncle = grandparent.left

        # red uncle and red parent: recolor
        if node.parent.color == "R" and uncle is not None and uncle.color == "R":
            node.parent.color = "B"
            uncle.color = "B"
            grandparent.color = "R"
            self.insertion_fixup(grandparent)
            return

        
        if self.is_left_child(node.parent):
            
            if self.is_left_child(node): # black uncle and red parent: simple rotation (LL) 
                self.simple_right_rotation(node, grandparent)
            else:                           
                self.double_left_right_rotation(node, grandparent)
            return

        # black uncle and red parent: simple rotation (RR) 
        if self.is_right_child(node.parent):

            if self.is_right_child(node):
                self.simple_left_rotation(node, grandparent)
            else:
                self.double_right_left_rotation(node, grandparent)
            return
        
    # LL
    def simple_right_rotation(self, node, grandparent):
        old_parent = node.parent
        old_grandparent = grandparent
        self.rotate_right(grandparent)
        old_parent.color = "B"
        old_grandparent.color = "R"
        
    # LR
    def double_left_right_rotation(self, node, grandparent):
        old_parent = node.parent
        old_grandparent = grandparent
        self.rotate_left(node.parent) 
        self.rotate_right(grandparent)
        old_grandparent.color = "R"
        old_parent.color = "R"
        node.color = "B"

    # RR
    def simple_left_rotation(self, node, grandparent):
        old_parent = node.parent
        old_grandparent = grandparent
        self.rotate_left(grandparent)
        old_parent.color = "B"
        old_grandparent.color = "R"

    # RL
    def double_right_left_rotation(self, node, grandparent):
        old_parent = node.parent
        old_grandparent = grandparent
        self.rotate_right(node.parent) 
        self.rotate_left(grandparent)
        old_grandparent.color = "R"
        old_parent.color = "R"
        node.color = "B"    

    def search(self, target: int) -> Node | None:
        if self.root is None:
            return None

        current = self.root

        while current is not None:
            if target == current.value:
                return current
            elif target < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, target: int):
        node = self.search(target)

        if node is None:
            return

        # no childs
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
                return

            if self.is_left_child(node):
                node.parent.left = None
            else:
                node.parent.right = None
                
            node.parent = None

        # two childs
        elif node.left is not None and node.right is not None:
            pass

        # one child on left or right
        else:
            # handle case where the target is the root
            if node.parent is None:
                if node.left is None:
                    self.root = node.right
                    node.right.parent = None
                    node.right = None
                    
                else:
                    self.root = node.left
                    node.left.parent = None
                    node.left = None
                return

            # decide whether node has right child
            if node.left is None:

                # the right child points to the new parent
                node.right.parent = node.parent

                # decide whether the node is a left child or right child
                if self.is_left_child(node):
                    node.parent.left = node.right
                    
                else:
                    node.parent.right = node.right

            # decie whether node has a left child
            else:
                # the left child points to the new parent
                node.left.parent = node.parent

                # decide whether the node is a left child or right child
                if self.is_right_child(node):
                    node.parent.right = node.left

                else:
                    node.parent.left = node.left

            # both references within current node are removed
            node.parent = None
            node.right = None
            node.left = None

        