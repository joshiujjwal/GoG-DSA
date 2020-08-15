import sys

class BSTNode:
    def __init__(self, data):
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
            curr = curr.left
        else:
            if curr.data > key:
                curr = curr.right
            else:
                return
    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.left = BSTNode(key)
    return root

class pairSum:
    def __init__(self):
        self.sumSet = set()
    
    def pair(self, root, s):
        if root is None:
            return False
        self.pair(root.left, s)
        if (s - root.data) in self.sumSet:
            return True
        else:
            self.sumSet.add(root.data)
        return self.pair(root.right, s)

    


if __name__ == "__main__":
    bst = BSTNode(20)
    insert_iterative(bst, 10)
    insert_recursive(bst, 15)
    insert_recursive(bst, 25)
    insert_recursive(bst, 30)
    print(pairSum().pair(bst, 100))



