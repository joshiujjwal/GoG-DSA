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
    parent = None
    curr = root
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


def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if root.data < key:
        return search(root.right,key)
    else:
        return search(root.left, key)

if __name__ == "__main__":
    bst = BSTNode(50)
    insert_recursive(bst, 30)
    insert_iterative(bst, 70)
    print(bst.data)
    print(bst.right.data)
    print(bst.left.data)
    print(search(bst,90))