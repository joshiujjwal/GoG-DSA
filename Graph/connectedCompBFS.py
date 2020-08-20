class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [None] * vertices

    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph():
        for i in self.vertices:
            print(str(i)+" --> ")
            j = self.graph[i]
            while j:
                print(j.data,end=" ")
                j = j.next
            print('\n')

def BFS(g, root, visited):
    Q = []
    Q.append(root)
    visited[root] = True
    while(len(Q)):
        res = Q.pop(0)
        #print(res)
        while(g.graph[res]):
            if visited[g.graph[res].data] == False:
                Q.append(g.graph[res].data)
                visited[g.graph[res].data] = True
            g.graph[res] = g.graph[res].next 
    return visited

if __name__ == "__main__":
    g = Graph(9)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(5,6)
    g.addEdge(5,7)
    g.addEdge(8,8)
    #g.printGraph
    visited = [False]*g.vertices
    connectCount = 0
    for i in range(g.vertices):
        if visited[i] == False:
            visited = BFS(g,i,visited)
            connectCount+=1
    print("Connect Components: ",connectCount)