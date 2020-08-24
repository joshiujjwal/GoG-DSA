class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [None] * vertices
    
    def addEdge(self,src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

def detectCycle(g, root, visited, parent):
    visited[root] = True
    while(g.graph[root]):
        if visited[g.graph[root].data] == False:
            detectCycle(g, g.graph[root].data, visited, root)
        else:
            if parent != root:
                return True
        g.graph[root] = g.graph[root].next
    return False




if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(0,4)
    visited = [False] * g.vertices
    print(detectCycle(g, 0, visited, -1))