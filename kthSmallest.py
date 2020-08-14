# considering balanced binary tree 

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.lcount = 0

def insert_recursive(root,key):
    if root is None:
        return BSTNode(key)
    if root.data == key:
        return
    if root.data < key:
        root.right = insert_recursive(root.right, key)
    else:
        root.lcount+=1
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
                parent.lcount +=1 
                curr = curr.left
            else:
                return
    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.lcount +=1 
        parent.left = BSTNode(key)
    return root

def kSmallest(root, k):
    if root is None:
        return 
    if root.lcount + 1 == k:
        return root.data
    else:
        if root.lcount + 1 < k:
            return kSmallest(root.right, k - root.lcount - 1)
        else:
            return kSmallest(root.left, k)
    return None     
if __name__ == "__main__":
    bst = BSTNode(50)
    insert_recursive(bst, 40)
    insert_recursive(bst, 60)
    insert_recursive(bst, 55)
    insert_recursive(bst, 20)
    print(kSmallest(bst, 1))
    print(kSmallest(bst, 2))
    print(kSmallest(bst, 3))
    print(kSmallest(bst, 4))
    print(kSmallest(bst, 5))

