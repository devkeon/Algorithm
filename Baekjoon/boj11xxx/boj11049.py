n = int(input())
matrix = [[*map(int, input().split(" "))] for _ in range(n)]

dp = [[0 for _ in range(n)] for j in range(n)]

for r in range(1, n):
    for i in range(n - r):
        j = i + r
        dp[i][j] = min(dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1] for k in range(i, j))
print(dp[0][n - 1])
