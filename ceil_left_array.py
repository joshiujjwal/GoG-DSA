# ceil with self balance bst, time complexity is greater On(n*n)
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert_recursive(root, key):
    if root is None:
        return BSTNode(key)
    if root == key:
        return 
    if root.data < key:
        root.right = insert_recursive(root.right, key)
    else:
        root.left = insert_recursive(root.left, key)
    return root

def insert_iterative(root,key):
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

def ceil(root, key):
    if root is None:
        return root
    curr = root
    ceil_val = -1
    while(curr is not None):
        if curr.data < key:
            curr = curr.right
        else:
            if curr.data > key:
                ceil_val = curr.data
                curr = curr.left
            else:
                break         
    return ceil_val

if __name__ == "__main__":
    arr = [2,8,30,15,25,12]
    bst = BSTNode(arr[0])
    print(-1, end=" ")
    for i in range(1,len(arr)):
        insert_recursive(bst, arr[i])
        print(ceil(bst, arr[i]), end=" ")
