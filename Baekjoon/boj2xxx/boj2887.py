import sys
import heapq

read = sys.stdin.readline

n = int(read())
parent = [int(i) for i in range(n)]
xdist, ydist, zdist = [], [], []


def find(k):
    if k == parent[k]:
        return k
    parent[k] = find(parent[k])
    return parent[k]


def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return True
    elif px > py:
        parent[px] = py
    else:
        parent[py] = px
    return False


for i in range(n):
    x, y, z = map(int, read().split())
    xdist.append([x, i])
    ydist.append([y, i])
    zdist.append([z, i])

xdist.sort()
ydist.sort()
zdist.sort()
heap = []
for i in range(n - 1):
    xd = abs(xdist[i][0] - xdist[i + 1][0])
    yd = abs(ydist[i][0] - ydist[i + 1][0])
    zd = abs(zdist[i][0] - zdist[i + 1][0])
    heapq.heappush(heap, [xd, xdist[i][1], xdist[i + 1][1]])
    heapq.heappush(heap, [yd, ydist[i][1], ydist[i + 1][1]])
    heapq.heappush(heap, [zd, zdist[i][1], zdist[i + 1][1]])

cnt = 0
ans = 0
while cnt < n - 1:
    dist, x, y = heapq.heappop(heap)
    if union(x, y):
        continue
    ans += dist
    cnt += 1

print(ans)
