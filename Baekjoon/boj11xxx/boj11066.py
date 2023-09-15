import sys
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    k = int(read())
    page = [*map(int, read().split(" "))]
    dp = [[0 for _ in range(k)] for _ in range(k)]
    s = [0 for _ in range(k + 1)]
    for j in range(1, k + 1):
        s[j] = s[j - 1] + page[j - 1]
    for r in range(1, k):
        for i in range(k - r):
            j = i + r
            dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j)) + (s[j + 1] - s[i])
    print(dp[0][k - 1])
