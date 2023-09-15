import sys
import heapq
read = sys.stdin.readline

n, m, x = map(int, read().split(" "))
fgraph = [[] for _ in range(n)]
tgraph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, read().split(" "))
    fgraph[u - 1].append([v - 1, c])
    tgraph[v - 1].append([u - 1, c])


def dijkstra(s, dist, mapp):
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        curdist, curdest = heapq.heappop(heap)
        if dist[curdest] < curdist:
            continue
        for nxdest, nxdist in mapp[curdest]:
            cost = curdist + nxdist
            if cost < dist[nxdest]:
                dist[nxdest] = cost
                heapq.heappush(heap, (cost, nxdest))


go_dist = [1000001 for _ in range(n)]
back_dist = [1000001 for _ in range(n)]

dijkstra(x - 1, go_dist, tgraph)
dijkstra(x - 1, back_dist, fgraph)

ans = 0
for i in range(n):
    ans = max(ans, go_dist[i] + back_dist[i])

print(ans)
