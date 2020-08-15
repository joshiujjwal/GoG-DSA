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
        root.right = insert_recursive(root.right,key)
    else:
        root.left = insert_recursive(root.left,key)
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
                return root
    
    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.left = BSTNode(key)
    return root

def get_successor(curr):
    curr = curr.right
    while(curr is not None and curr.left is not None):
        curr = curr.left
    return curr


def delete(root, key):
    if root is None:
        return root
    if root.data < key:
        root.right = delete(root.right, key)
    else:
        if root.data > key:
            root.left = delete(root.left, key)
        else:
            if root.left is None:
                temp = root.right
                del root
                return temp
            else:
                if root.right is None:
                    temp = root.left
                    del root
                    return temp
                else:
                    successor = get_successor(root)
                    root.data = successor.data
                    root.right = delete(root.right, successor.data)
    return root

if __name__ == "__main__":
    bst = BSTNode(50)
    insert_recursive(bst, 70)
    insert_recursive(bst, 30)
    insert_recursive(bst, 60)
    insert_recursive(bst, 80)
    insert_recursive(bst, 55)
    insert_recursive(bst, 16)
    insert_recursive(bst, 40)
    delete(bst, 30)
    print(bst.data)
    print(bst.right.right.data)
    print(bst.left.left.data)
    