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

def topologicalSort(g,indegree):
    Q = []
    for i in range(g.vertices):
        if indegree[i] == 0:
            Q.append(i)
    while(len(Q)):
        res = Q.pop(0)
        print(res)
        while(g.graph[res]):
            indegree[g.graph[res].data]-=1
            if indegree[g.graph[res].data] == 0:
                Q.append(g.graph[res].data)
            g.graph[res] = g.graph[res].next


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,3)
    g.addEdge(1,4)
    indegree = [0] * g.vertices
    for i in g.graph:
        while(i):
            indegree[i.data] +=1
            i = i.next
    
    topologicalSort(g,indegree)
