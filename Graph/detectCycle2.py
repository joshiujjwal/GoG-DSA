class AdjNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None]*vertices

    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

def detectCycle(g,indegree):
    Q = []
    count = 0
    for i in indegree:
        if indegree[i] == 0:
            Q.append(i)
    while(len(Q)):
        res = Q.pop(0)
        count +=1
        while(g.graph[res]):
            indegree[g.graph[res].data] -=1
            if indegree[g.graph[res].data] == 0:
                Q.append(g.graph[res].data)
            g.graph[res] = g.graph[res].next
    return count != g.vertices
if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    indegree = [0]*g.vertices
    for i in g.graph:
        while(i):
            indegree[i.data]+=1
            i = i.next
    print(detectCycle(g,indegree))