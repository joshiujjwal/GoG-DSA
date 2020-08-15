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

class vSum:
    def __init__(self):
        self.vMap = {}
    
    def verticalSum(self, root, h):
        if root is None:
            return
        self.verticalSum(root.left, h-1)
        if h in self.vMap:
            self.vMap[h] += root.data
        else:
            self.vMap[h] = root.data
        self.verticalSum(root.right, h+1)
    
    def vSum(self, root):
        self.verticalSum(root, 0)
        for i in self.vMap.values():
            print(i, end=" ")



if __name__ == "__main__":
    bst = BSTNode(10)
    insert_recursive(bst, 15)
    insert_recursive(bst, 25)
    insert_recursive(bst, 30)
    insert_recursive(bst, 20)
    vSum().vSum(bst)
