class AdjNode:
    def __init__(self,data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.graph = [None] * vertices
        self.vertices = vertices
    
    def addEdge(self, source, dest):
        node = AdjNode(dest)
        node.next = self.graph[source]
        self.graph[source] = node


        node = AdjNode(source)
        node.next = self.graph[dest]
        self.graph[dest] = node


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    print(g.graph[0].data)
    print(g.graph[1].next.data)
