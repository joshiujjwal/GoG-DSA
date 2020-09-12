import sys
class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*vertices
        self.weight = {}
    
    def addEdge(self, src, dest, weight):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        self.weight[str(src)+str(dest)] = weight

def topoSortUtil(g, root, visited, stk):
    visited[root] = True
    i = g.graph[root]
    while(i):
        if visited[i.data] == False:
            topoSortUtil(g, i.data, visited, stk)
        i = i.next
    stk.append(root)


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0,1,2)
    g.addEdge(0,4,1)
    g.addEdge(1,2,3)
    g.addEdge(2,3,6)
    g.addEdge(4,2,2)
    g.addEdge(4,5,4)
    g.addEdge(5,3,1)
    visited = [False]*g.vertices
    stk = []
    dist = [sys.maxsize] * g.vertices 
    topoSortUtil(g, 0, visited, stk)
    dist[0] = 0 
    for i in stk[::-1]:
        root = i
        while(g.graph[i]):
            if dist[g.graph[i].data] > dist[root] + g.weight[str(root)+str(g.graph[i].data)]:
                dist[g.graph[i].data] = dist[root] + g.weight[str(root)+str(g.graph[i].data)]
            g.graph[i] = g.graph[i].next
    print(dist)

