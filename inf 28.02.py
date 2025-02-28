# упражение 1
import numpy as np

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def matrix_smezh(self, vert):
        A = [[float("Inf")] * vert for i in range(vert)]
        for _ in range(self.V):
            for s, d, w in self.graph:
                A[s][d] = w
                A[s][s] = 0
                A[d][d] = 0
        return (A)

    def print_solution(self, dist):
        for i in range(self.V - 1):
            print(i, 'до этой вершины расстояние', dist[i])

    def bellman_ford(self, src):
        pr = []
        dist = [float("Inf")] * self.V
        dist[src] = 0
        fl = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Возможно")
                fl = 1
        if fl == 0:
            print("Невозможно")
        return

        self.print_solution(dist)


c = int(input())
for i in range(c):
    n, m = list(map(int, input().split()))
    g = Graph(n)
    for q in range(m):
        x, y, t = list(map(int, input().split()))
        g.add_edge(x, y, t)
    g.bellman_ford(0)

# упражнение 2


def distance_matrix(points):
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = np.sqrt(
                (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
    return distance_matrix


def floyd(A, V):
    for j in range(V):
        for u in range(V):
            for v in range(V):
                distance = A[u][j] + A[j][v]
                if distance < A[u][v]:
                    A[u][v] = distance
    return A


n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split()))
    lst = [x, y]
    points.append(lst)
A = distance_matrix(points)
shortest = floyd(A, n)
print(shortest[0][n-1])
