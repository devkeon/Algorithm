import sys
read = sys.stdin.readline

n = int(read())
seq = [*map(int, read().split())]
m = int(read())
dp = [[0 for _ in range(n)] for k in range(n)]
for i in range(2):
    for j in range(n - i):
        if seq[j] == seq[j + i]:
            dp[j][j + i] = 1

for i in range(2, n):
    for j in range(n - i):
        if seq[j] == seq[j + i] and dp[j + 1][j + i - 1] == 1:
            dp[j][j + i] = 1

for _ in range(m):
    s, e = map(int, read().split())
    print(dp[s - 1][e - 1])
