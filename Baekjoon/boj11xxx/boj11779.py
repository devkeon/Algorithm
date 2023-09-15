import sys
import heapq

read = sys.stdin.readline
maxim = float("inf")
n = int(read())
m = int(read())
graph = [[] for _ in range(n)]


def dijkstra(start, end):
    dist = [maxim for _ in range(n)]
    dist[start] = 0
    p = [[] for _ in range(n)]
    p[start] = [start + 1]
    heap = []
    heapq.heappush(heap, [0, start, [start + 1]])
    while heap:
        curdist, curdest, curpath = heapq.heappop(heap)
        if dist[curdest] < curdist:
            continue
        for nxtdist, nxtdest in graph[curdest]:
            cost = nxtdist + curdist
            if cost < dist[nxtdest]:
                dist[nxtdest] = cost
                npath = curpath + [nxtdest + 1]
                p[nxtdest] = npath
                heapq.heappush(heap, [cost, nxtdest, npath])
    return dist[end], p[end]


for _ in range(m):
    u, v, c = map(int, read().split())
    graph[u - 1].append([c, v - 1])

s, e = map(int, read().split())
cnt, ans = dijkstra(s - 1, e - 1)
print(cnt)
print(len(ans))
print(*ans)
