import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
n = int(read())
graph = [[] for _ in range(n)]
ans = [0 for _ in range(n)]
visit = [False for _ in range(n)]
for _ in range(n):
    tmp = [*map(int, read().split())]
    cur = tmp[0] - 1
    for i in range(1, len(tmp) - 1, 2):
        graph[cur].append([tmp[i] - 1, tmp[i + 1]])


def dfs(v, dist):
    for nxt, cost in graph[v]:
        if not visit[nxt]:
            visit[nxt] = True
            ans[nxt] = dist + cost
            dfs(nxt, dist + cost)


visit[0] = True
dfs(0, 0)
t = ans.index(max(ans))
visit = [False for _ in range(n)]
ans = [0 for _ in range(n)]
visit[t] = True
dfs(t, 0)
print(max(ans))
