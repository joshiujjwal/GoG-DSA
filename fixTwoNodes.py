import sys
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert_recursive(root, key):
    if root is None:
        return BSTNode(key) 
    if root.data == key:
        return    
    if root.data < key:
        root.right = insert_recursive(root.right, key)
    else:
        root.left = insert_recursive(root.left, key)
    return root

def insert_iterative(root, key):
    curr = root
    parent = None
    while curr is not None:
        parent = curr
        if curr.data < key:
            curr = curr.right
        else:
            if curr.data > key:
                curr = curr.left
            else:
                return 
    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.left = BSTNode(key)
    return root

class fixNode:

    def __init__(self):
        self.prev = BSTNode(sys.maxsize)
        self.first = BSTNode(sys.maxsize)
        self.second = BSTNode(sys.maxsize)
    
    def findNodes(self, root):
        if root is None:
            return
        self.findNodes(root.left)
        if root.data < self.prev.data and self.prev.data != sys.maxsize:
            if self.first.data == sys.maxsize:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.findNodes(root.right)
    
    def swapNode(self, root):
        self.findNodes(root)
        self.first.data, self.second.data = self.second.data, self.first.data
        return root

def inorderBST(root):
    if root is None:
        return
    else:
        inorderBST(root.left)
        print(root.data, end=" ")
        inorderBST(root.right)


if __name__ == "__main__":
    bst = BSTNode(20)
    insert_iterative(bst, 15)
    insert_recursive(bst, 40)
    insert_recursive(bst, 30)
    insert_iterative(bst, 50)
    insert_recursive(bst, 5)
    inorderBST(bst)
    print("\n")
    bst.right.data = 15
    bst.left.data = 40
    inorderBST(bst)
    print("\n")
    fixNode().swapNode(bst)
    inorderBST(bst)