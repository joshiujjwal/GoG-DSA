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


        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):
        for i in range(self.vertices):
            j = self.graph[i]
            print(str(i) + " --> ", end="")
            while j:
                print(j.data, end=" ")
                j = j.next
            print(' \n')


def BFS(g, root, visited):
    Q = []
    Q.append(root)
    visited[root] = True
    while(len(Q)):
        res = Q.pop(0)
        print(res)        
        while(g.graph[res]):
            if visited[g.graph[res].data] == False:
                Q.append(g.graph[res].data)
                visited[g.graph[res].data] = True
            g.graph[res] = g.graph[res].next


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(2,3)
    g.addEdge(3,4)

    #g.printGraph()
    visited = [False]*8
    BFS(g,0,visited)
