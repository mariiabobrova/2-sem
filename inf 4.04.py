#упражнение 1
class Graph:

    def __init__(self, graph):
        self.graph = graph  
        self.ROW = len(graph)
    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u 
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0  
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  
                self.graph[v][u] += path_flow  
                v = parent[v]
        return max_flow


n = int(input())
k = 0
while n != 0:
    k += 1
    s, t, c = list(map(int, input().split()))
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(c):
        a, b, l = list(map(int,input().split()))
        graph[a-1][b-1] = l
        graph[b-1][a-1] = l
    g = Graph(graph)
    print("Network %d" % k) 
    print("The bandwith is %d" % g.FordFulkerson(s, t))
n = int(input())
    