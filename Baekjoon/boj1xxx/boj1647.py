import sys

read = sys.stdin.readline

n, m = map(int, read().split())
roads = []
parent = [int(i) for i in range(n)]

for _ in range(m):
    u, v, c = map(int, read().split())
    roads.append([c, u - 1, v - 1])
roads.sort()
cut = 0
ans = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    xp = find(x)
    yp = find(y)
    if xp < yp:
        parent[y] = xp
    elif xp > yp:
        parent[x] = yp
    else:
        return False
    return True


for cost, u, v in roads:
    x = find(u)
    y = find(v)
    if union(x, y):
        ans += cost
        cut = max(cut, cost)

print(ans - cut)
