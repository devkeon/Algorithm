import sys
sys.setrecursionlimit(10**7)
read = sys.stdin.readline
mr = [-1, 0, 1, 0]
mc = [0, -1, 0, 1]
m, n = map(int, read().split(" "))
hill = [list(map(int, read().split(" "))) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]


def dfs(row, col):
    if row == m - 1 and col == n - 1:
        return 1
    if dp[row][col] > -1:
        return dp[row][col]
    dp[row][col] = 0
    for i in range(4):
        nr = row + mr[i]
        nc = col + mc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if hill[row][col] > hill[nr][nc]:
                dp[row][col] += dfs(nr, nc)
    return dp[row][col]


print(dfs(0, 0))
