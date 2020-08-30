class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices
    
    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

def topologicalSortDFS(g, root, visited, stk):
    visited[root] = True
    while(g.graph[root]):
        if visited[g.graph[root].data] == False:
            topologicalSortDFS(g,g.graph[root].data, visited, stk)
        g.graph[root] = g.graph[root].next
    stk.append(root)



if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,3)
    g.addEdge(1,4)
    visited = [False]*g.vertices
    stk = []
    for i in range(0,g.vertices):
        if visited[i] == False:
            topologicalSortDFS(g,i,visited,stk)
    for i in reversed(stk):
        print(i)