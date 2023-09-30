import sys
read = sys.stdin.readline

n = int(read())
lines = [[*map(int, read().split())] for _ in range(n)]
graph = [[301 for _ in range(n)] for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if lines[j][0] <= lines[i][0] <= lines[j][1] or lines[j][0] <= lines[i][1] <= lines[j][1]\
                or lines[i][0] <= lines[j][0] <= lines[i][1] or lines[i][0] <= lines[j][1] <= lines[i][1]:
            graph[i][j] = 1
            graph[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            graph[j][i] = min(graph[j][i], graph[j][k] + graph[k][i])
q = int(read())
for _ in range(q):
    a, b = map(int, read().split())
    print(graph[a - 1][b - 1] if graph[a - 1][b - 1] != 301 else -1)
