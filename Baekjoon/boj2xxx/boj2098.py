import sys

read = sys.stdin.readline
MAX = 17000001
n = int(read())
w = [[*map(int, read().split(" "))] for _ in range(n)]
dp = [[MAX for _ in range(1 << n)] for _ in range(n)]
fin = (1 << n) - 1


def dfs(cur, node):
    if cur == fin:
        if w[node][0] == 0:
            return MAX
        else:
            return w[node][0]
    if dp[node][cur] != MAX or dp[node][cur] == 17000002:
        return dp[node][cur]
    for i in range(1, n):
        if cur & (1 << i) or w[node][i] == 0:
            continue
        dp[node][cur] = min(dp[node][cur], dfs(cur | (1 << i), i) + w[node][i])
    if dp[node][cur] == MAX:
        dp[node][cur] = 17000002
    return dp[node][cur]


print(dfs(1, 0))
