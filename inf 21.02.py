# упражнение 1
import collections
import sys


def all_vertex(graf):
    return list(graf.keys())


def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())


def value(graf, vertex1, vertex2):
    return (graf[vertex1][vertex2])


def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}
    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0
    while unvisited_vertexes:
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex == None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_vertex] + \
                value(graf, current_min_vertex, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path


def print_result(previous_vertex, shortest_path,
                 start_vertex, target_vertex):
    path = []
    vertex = target_vertex
    while vertex != start_vertex:
        path.append(vertex)
        vertex = previous_vertex[vertex]
    path.append(start_vertex)
    print("->".join(reversed(path)))
    print(shortest_path[target_vertex])


n, m, s, f = list(map(int, input().split()))
edges = []  # ввод вершин и длины ребра
graph = {}
for start, end, weight in edges:
    if start not in graph:
        graph[start] = []
    graph[start].append((end, weight))
previous_vertex, shortest_path = dijkstra(graph, s)
print_result(previous_vertex, shortest_path, s, f)


# упражнение 2
def is_cyclic(graph_array: list[list[int]]) -> bool:
    used = [False] * len(graph_array)
    res = False

    def dfs(v, p=-1):
        used[v] = True
        for u in graph_array[v]:
            if not used[u]:
                dfs[u, v]
            elif u != p:
                res = True
                break

    for i in range(len(graph_array)):
        if not used[i]:
            dfs[i]
    return res

graph = []  # Ввод списка смежности
v, e = list(map(int, input().split()))
if is_cyclic(graph) == True:
    print("YES")
else:
    print("NO")

# упражнение 3
def meetings(start, end):
    mt = sorted((start, end), key=lambda x: x[1])
    k = 0
    last = 0
    for a, b in mt:
        if a >= last:
            k += 1
            last = b
    return k

n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
print(meetings(start, end))

# упражнение 5
def bfs(n, k):
    graph = []
    for u, v in k:
        graph[u].append(v)
        graph[v].append(u)
    distances = [-1] * n
    distances[0] = 0
    queue = collections.deque([0])
    while queue:
        cur = queue.popleft()
        cur_distance = distances[cur]
        for l in graph[cur]:
            if distances[l] == -1:
                distances[l] = cur_distance + 1
                queue.append(l)
    return distances

n, m = list(map(int, input().split()))
edges = [tuple(map(int, input().strip().split())) for p in range(m)]
distances = bfs(n, k)
for i in distances:
    print(i)
