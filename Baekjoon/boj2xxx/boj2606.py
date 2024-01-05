import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
m = int(read())
graph = [[] for _ in range(n)]
visit = [False for _ in range(n)]
for _ in range(m):
    a, b = map(int, read().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dq = deque()
dq.append(0)
visit[0] = True
cnt = 0

while dq:
    cur = dq.popleft()
    for nxt in graph[cur]:
        if not visit[nxt]:
            dq.append(nxt)
            cnt += 1
            visit[nxt] = True

print(cnt)
