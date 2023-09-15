import sys
import math

read = sys.stdin.readline

n = int(read())
stars = [[*map(float, read().split())] for _ in range(n)]
dist = []
parent = [int(i) for i in range(n)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(px, py):
    if px > py:
        parent[px] = py
    else:
        parent[py] = px


for i in range(n):
    for j in range(i + 1, n):
        u, v = stars[i], stars[j]
        distance = math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
        dist.append([distance, i, j])
dist.sort()
ans = 0
for cost, n1, n2 in dist:
    p1 = find(n1)
    p2 = find(n2)
    if p1 != p2:
        union(p1, p2)
        ans += cost
print(round(ans, 2))
