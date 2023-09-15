import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split(" "))
line = [[] for _ in range(n)]
indegree = [0 for _ in range(n)]
dq = deque()
ans = []

for i in range(m):
    u, v = map(int, read().split(" "))
    line[u - 1].append(v - 1)
    indegree[v - 1] += 1

for i in range(n):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    cur = dq.popleft()
    ans.append(cur + 1)
    for nxt in line[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            dq.append(nxt)

print(*ans)

