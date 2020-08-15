
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def insert_recursive(root,key):
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
    while(curr is not None):
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

def preorderBST(root):
    if root is None:
        return
    else:
        print(root.data)
        preorderBST(root.left)
        preorderBST(root.right)
    

    return None     
if __name__ == "__main__":
    bst = BSTNode(50)
    insert_recursive(bst, 40)
    insert_recursive(bst, 60)
    insert_recursive(bst, 55)
    insert_recursive(bst, 20)
    preorderBST(bst)

