import sys

read = sys.stdin.readline

n, m = map(int, read().split())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, c = map(int, read().split())
    tree[u - 1].append([v - 1, c])
    tree[v - 1].append([u - 1, c])


def dfs(node, dist, dst):
    global visit
    for nxt, cost in tree[node]:
        if nxt == dst:
            global ans
            ans = dist + cost
            return
        if not visit[nxt]:
            visit[nxt] = True
            dfs(nxt, dist + cost, dst)


for _ in range(m):
    visit = [False for _ in range(n)]
    ans = 0
    u, v = map(int, read().split())
    visit[u - 1] = True
    dfs(u - 1, 0, v - 1)
    print(ans)
