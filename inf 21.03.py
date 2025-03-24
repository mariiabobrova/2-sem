# упражнение 1
def dfs(start, visited, g, ok):
    if visited[start] == 0:
        visited[start] = 1
    for u in g[start]:
        ok.append(visited[u] == visited[start])
        if visited[u] == 0:
            if visited[start] == 1:
                visited[u] = 2
            elif visited[start] == 2:
                visited[u] = 1
            dfs(u, visited, g, ok)

    return ok


with open("INPUT.TXT") as f:
    N, M = map(int, f.readline().strip().split())
    graph = [[] for i in range(N)]
    for l in range(M):
        u, v = map(int, f.readline().strip().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)


visited = [0] * N
ok = dfs(1, visited, graph, [])

if max(ok):
    str = "NO"
else:
    str = "YES"

with open("OUTPUT.TXT", "w") as f:
    f.write(str)

# упражнение 3
n = 6
result = 1
for i in range(1, n, 2):
    result *= i
print(result)  # Вывод: 15 паросочетаний
