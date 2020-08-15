#Approach One (Wrong)
# Check only for each node and its children

#Approach Two
# Check for max in left subtree and min in right subtree and compare that, i case of skewed higher complexity

#Approach Three
# Check for range for each node id satify okay else false

#Approach Four
# Check for inorder traversal is sorted order
# 
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

def checkBST(root, prev):
    if root is None:
        return True
    else:
        if checkBST(root.left, prev) == False:
            return False
        if root.data <= prev:
            return False
        prev = root.data
        return checkBST(root.right, prev)
    return True
    


if __name__ == "__main__":
    bst = BSTNode(20)
    insert_iterative(bst, 10)
    insert_recursive(bst, 15)
    insert_recursive(bst, 25)
    insert_recursive(bst, 30)
    bst.right.left = BSTNode(21)
    print(checkBST(bst, -sys.maxsize))


