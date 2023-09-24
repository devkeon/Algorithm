import sys

read = sys.stdin.readline

g = int(read())
p = int(read())
parent = [int(i) for i in range(g + 1)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px


ans = 0
for _ in range(p):
    i = int(read())
    tmp = find(i)
    if tmp == 0:
        break
    union(tmp, tmp - 1)
    ans += 1
print(ans)
