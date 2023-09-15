import sys
import heapq

read = sys.stdin.readline

n, m, r = map(int, read().split(" "))
items = [*map(int, read().split(" "))]
roads = [[] for _ in range(n)]

for _ in range(r):
    u, v, c = map(int, read().split(" "))
    roads[u - 1].append([v - 1, c])
    roads[v - 1].append([u - 1, c])


def djikstra(src):
    dist = [1501 for _ in range(n)]
    heap = []
    tmp = 0
    dist[src] = 0
    heapq.heappush(heap, [0, src])
    while heap:
        curd, cur = heapq.heappop(heap)
        for nxt, cost in roads[cur]:
            ncost = curd + cost
            if dist[nxt] > ncost:
                dist[nxt] = ncost
                heapq.heappush(heap, [dist[nxt], nxt])
    for i in range(n):
        if dist[i] <= m:
            tmp += items[i]
    return tmp


ans = 0
for j in range(n):
    ans = max(ans, djikstra(j))

print(ans)
