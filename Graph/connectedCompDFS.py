class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    def addEdge(self, src, dest):
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

def DFS(g, root, visited):
    visited[root] = True
    while(g.graph[root]):
        if visited[g.graph[root].data] == False:
            DFS(g,g.graph[root].data, visited)
        g.graph[root] = g.graph[root].next


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(3,2)
    g.addEdge(2,4)
    visited = [False]*5
    count = 0
    for i in range(5):
        if visited[i] == False:
            DFS(g, i, visited)
            count +=1    
    print(count)
