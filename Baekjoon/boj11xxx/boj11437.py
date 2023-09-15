import sys

sys.setrecursionlimit(10 ** 5)

read = sys.stdin.readline
n = int(read())
tree = [[] for _ in range(n)]
ancestor = [0 for _ in range(n)]
level = [0 for _ in range(n)]
visit = [False for _ in range(n)]
visit[0] = True
for _ in range(n - 1):
    p, c = map(int, read().split())
    tree[p - 1].append(c - 1)
    tree[c - 1].append(p - 1)


def ca(node, lv):
    level[node] = lv
    for nxt in tree[node]:
        if not visit[nxt]:
            visit[nxt] = True
            ancestor[nxt] = node
            ca(nxt, lv + 1)


def find(u, v):
    while level[u] != level[v]:
        if level[u] > level[v]:
            u = ancestor[u]
        else:
            v = ancestor[v]
    while u != v:
        u = ancestor[u]
        v = ancestor[v]
    return u + 1


ca(0, 0)
m = int(read())
for _ in range(m):
    x, y = map(int, read().split())
    print(find(x - 1, y - 1))
