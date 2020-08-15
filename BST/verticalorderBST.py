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

class vOrder:
    def __init__(self):
        self.vMap = {}
    
    def verticalOrder(self, root, h):
        if root is None:
            return
        self.verticalOrder(root.left, h-1)
        if h in self.vMap:
            self.vMap[h].append(root.data)
        else:
            self.vMap[h] = [root.data]
        self.verticalOrder(root.right, h+1)
    
    def vOrder(self, root):
        self.verticalOrder(root, 0)
        for i in self.vMap.values():
            print(i)

def verticalOrderQ(root):
    if root is None:
        return
    else:
        Q = []
        vMap = {}
        hd= 0
        Q.append([hd, root])
        while(len(Q)):
            curr = Q.pop()
            if curr[0] not in vMap:
                vMap[curr[0]] = [curr[1].data]
            else:
                vMap[curr[0]].append(curr[1].data)
            if curr[1].left is not None:
                hd = curr[0]-1
                Q.append([hd, curr[1].left])
            if curr[1].right is not None:
                hd = curr[0]+1
                Q.append([hd,curr[1].right])
        for key, value in vMap.items():
            print(value)
        
        

if __name__ == "__main__":
    bst = BSTNode(10)
    insert_recursive(bst, 15)
    insert_recursive(bst, 25)
    insert_recursive(bst, 30)
    insert_recursive(bst, 20)
    vOrder().vOrder(bst)
    print("\n")
    verticalOrderQ(bst)
