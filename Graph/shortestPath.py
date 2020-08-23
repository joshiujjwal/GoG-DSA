import sys
class AdjNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]* vertices

    def addEgde(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src]  = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

def shortestPath(graph, root, visited):
    Q = []
    dist = [-sys.maxsize] * graph.vertices
    Q.append(root)
    dist[root] = 0 
    visited[root] = True
    while(len(Q)):
        res = Q.pop(0)
        while(graph.graph[res]):
            if visited[graph.graph[res].data] == False:
                Q.append(graph.graph[res].data)
                visited[graph.graph[res].data] = True
                dist[graph.graph[res].data] = dist[res] + 1
            graph.graph[res] = graph.graph[res].next
    return dist

if __name__ == "__main__":
    g = Graph(6)
    g.addEgde(0,1)
    g.addEgde(0,2)
    g.addEgde(1,3)
    g.addEgde(2,4)
    g.addEgde(4,5)
    visited = [False] * g.vertices
    print(shortestPath(g,0,visited))
    


