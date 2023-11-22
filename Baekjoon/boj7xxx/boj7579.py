import sys

read = sys.stdin.readline

n, m = map(int, read().split())
A = [*map(int, read().split())]
C = [*map(int, read().split())]
cost_sum = sum(C)
dp = [[0 for _ in range(cost_sum + 1)] for k in range(n)]
ans = 10001
for i in range(cost_sum + 1):
    if C[0] <= i:
        dp[0][i] = A[0]
        if dp[0][i] >= m:
            ans = min(ans, i)

for i in range(1, n):
    for c in range(cost_sum + 1):
        if C[i] > c:
            dp[i][c] = dp[i - 1][c]
        else:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - C[i]] + A[i])
        if dp[i][c] >= m:
            ans = min(ans, c)
print(ans)
