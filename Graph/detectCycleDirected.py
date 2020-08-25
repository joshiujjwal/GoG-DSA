class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    #Directed
    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

def detectCycle(g, root, visited, recArr):
    visited[root] = True
    recArr[root] = True
    while(g.graph[root]):
        if visited[g.graph[root].data] == False:
            return detectCycle(g, g.graph[root].data, visited, recArr)
        else:
            if recArr[g.graph[root].data] == True:
                return True
        g.graph[root] = g.graph[root].next
    return False

if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(3,2)
    g.addEdge(3,4)
    print(detectCycle(g,0,[False]*g.vertices,[False]*g.vertices))