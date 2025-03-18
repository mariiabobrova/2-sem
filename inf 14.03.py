# упражнение 1
import random
import time


def find_dfs(board, words):
    result = set()
    words = set(words)
    pref = set()
    M = len(board)
    L = len(board[0])

    def dfs(i, j, word, visited):
        if word in words:
            result.add(word)
        if (i < 0 or i >= M) or (j < 0 or j >= L):
            return None
        if (i, j) in visited:
            return None
        visited.add((i, j))
        now = board[i][j]
        if word + now in pref:
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    dfs(i + x, j + y, word + now, visited)
        visited.remove((i, j))
    for word in words:
        for i in range(1, len(word) + 1):
            pref.add(word[:i])
    for i in range(M):
        for j in range(L):
            dfs(i, j, "", set())
    return sorted(result)


N = int(input())
dictionary = input().split()
M, L = list(map(int, input().split()))
board = [input().split() for q in range(M)]
found = find_dfs(board, dictionary)
print(found)

# упражнение 2
# алгоритм Прима
def prim(G):
    INF = 10**10
    V = len(G)
    selected = [False]*V
    no_edge = 0
    selected[0] = True
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1

# алгоритм Краскала
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


def generate_test(n, m):
    edges = []
    vertex = [[] for q in range(n + 1)]
    for i in range(m):
        u = random.randint(1, n)
        v = random.randint(1, n)
        while v == u:
            v = random.randint(1, n)
        w = random.randint(1, 100)
        edges.append((u, v, w))
        vertex[u].append((v, w))
        vertex[v].append((u, w))
    return edges, vertex


def compare_time(g, tests):
    for i, (n, m) in tests:
        edges, vertex = generate_test(n, m)
        start_time = time.time()
        kruskal_weight = g.kruskal_algo(n, edges)
        kruskal_time = time.time() - start_time

        start_time = time.time()
        prim_weight = prim(n, edges, vertex)
        prim_time = time.time() - start_time

        print(f"Тест {i + 1}: n = {n}, m = {m}")
        print(f"Время = {kruskal_time:.6f} сек")
        print(f"Время = {prim_time:.6f} сек")

# упражнение 4
def dijkstra(graph, start, n):
    distances = []
    INF = 10 ** 10
    start = 0
    dist = [INF] * n
    dist[start] = 0
    used = [False] * n
    min_dist = 0
    min_vertex = start
    while min_dist < INF:
        i = min_vertex
        used[i] = True
        for j in range(n):
            if dist[j] > dist[i] + w[i][j]:
                dist[j] = dist[i] + w[i][j]
    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            min_vertex = j
            distances.append(min_dist)
    return (distances)


def main():
    data = input().split()
    x = 0
    n = int(data[x])
    m = int(data[x + 1])
    centers = list(map(int, data[(x + 2):(x + 2 + (len(data) - (x + 2)))]))
    x = x + len(centers) + 2
    graph = [[] for q in range(n)]
    for i in range(m):
        u = int(data[x])
        v = int(data[x + 1])
        w = int(data[x + 2])
        graph[u].append((v, w))
        graph[v].append((u, w))
        x += 3
    center_dist = {}
    for center in centers:
        center_dist[center] = dijkstra(graph, center, n)

    sum = 0
    for c in range(n):
        INF = 10**10
        min_dist = INF
        for center in centers:
            if center_dist[center][c] < min_dist:
                min_dist = center_dist[center][c]
        if min_dist <= INF:
            sum += min_dist
    print(sum)
