import sys
from collections import deque

read = sys.stdin.readline

t = int(read())

for _ in range(t):
    dq = deque()
    n, k = map(int, read().split(" "))
    indegree = [0 for _ in range(n)]
    loading = list(map(int, read().split(" ")))     # loading time
    graph = [[] for _ in range(n)]      # graph
    dp = [0 for _ in range(n)]
    for _ in range(k):
        s, e = map(int, read().split(" "))
        graph[s - 1].append(e - 1)
        indegree[e - 1] += 1
    dst = int(read()) - 1     # have to make
    for i in range(n):
        if indegree[i] == 0:
            dq.append(i)
            dp[i] = loading[i]
    while dq:
        now = dq.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                dq.append(nxt)
            dp[nxt] = max(dp[nxt], dp[now] + loading[nxt])
    print(dp[dst])
