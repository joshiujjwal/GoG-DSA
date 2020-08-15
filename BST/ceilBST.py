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
                return root

    if parent is None:
        return BSTNode(key)
    if parent.data < key:
        parent.right = BSTNode(key)
    else:
        parent.left = BSTNode(key)
    return root


def ceil(root, key):
    ceil_val = None
    if root is None:
        return root
    curr = root
    while (curr is not None):
        if curr.data < key:
            curr = curr.right
        else:
            ceil_val = curr.data
            curr = curr.left
    return ceil_val


if __name__ == "__main__":
    bst = BSTNode(10)
    insert_recursive(bst, 8)
    insert_recursive(bst, 16)
    insert_recursive(bst, 13)
    insert_recursive(bst, 20)
    print(bst.data)
    print(bst.right.data)
    print(bst.left.data)
    print(ceil(bst, 14))