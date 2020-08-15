class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert_recursive(root,key):
    if root is None:
        return BSTNode(key) 
    else:
        if root.data == key:
            return
        if root.data < key:
            root.right = insert_recursive(root.right,key)
        else:
            root.left = insert_recursive(root.left,key)
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
                return root
    
    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.left = BSTNode(key)
    return root

if __name__ == "__main__":
    bst = BSTNode(15)
    insert_recursive(bst, 16)
    insert_recursive(bst, 80)
    insert_recursive(bst, 12)
    insert_recursive(bst, 14)
    print(bst.left.right.data)

