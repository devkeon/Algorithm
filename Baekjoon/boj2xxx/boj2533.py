import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(read())
tree = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
ans = 0
dp = [[0, 1] for _ in range(n + 1)]


def rec(root):
    visit[root] = True
    for nxt in tree[root]:
        if visit[nxt]:
            continue
        rec(nxt)
        dp[root][0] += dp[nxt][1]
        dp[root][1] += min(dp[nxt][0], dp[nxt][1])


for _ in range(n - 1):
    u, v = map(int, read().split())
    tree[v].append(u)
    tree[u].append(v)
rec(1)
print(min(dp[1]))
