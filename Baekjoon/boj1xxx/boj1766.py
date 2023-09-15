import sys
import heapq
read = sys.stdin.readline

n, m = map(int, read().split())
quest = [[] for _ in range(n)]
indegree = [0 for _ in range(n)]
heap = []
ans = []
for i in range(m):
    s, e = map(int, read().split())
    quest[s - 1].append(e - 1)
    indegree[e - 1] += 1

for i in range(n):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    cur = heapq.heappop(heap)
    ans.append(cur + 1)
    for k in quest[cur]:
        indegree[k] -= 1
        if indegree[k] == 0:
            heapq.heappush(heap, k)

print(*ans)
