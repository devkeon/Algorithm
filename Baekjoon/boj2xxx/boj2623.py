import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
indegree = [0 for _ in range(n)]
graph = [[] for _ in range(n)]
dq = deque()
for _ in range(m):
    tmp = [*map(int, read().split())]
    for i in range(1, tmp[0]):
        graph[tmp[i] - 1].append(tmp[i + 1] - 1)
        indegree[tmp[i + 1] - 1] += 1
for i in range(n):
    if indegree[i] == 0:
        dq.append(i)
ans = []
while dq:
    cur = dq.popleft()
    ans.append(cur + 1)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            dq.append(nxt)

if len(ans) == n:
    print(*ans, sep='\n')
else:
    print(0)
