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

def DFS(graph,root, visited):    
    visited[root] = True
    print(root)
    while(graph.graph[root]):
        if visited[graph.graph[root].data] is False:
            DFS(graph,graph.graph[root].data,visited)
        graph.graph[root] = graph.graph[root].next

if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(0,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    visited =[False]*5
    DFS(g,0,visited)

    