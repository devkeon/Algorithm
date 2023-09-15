n = int(input())
seq = [*map(int, input().split())]
dp = [0 for _ in range(n)]

for i in seq:
    dp[i] = max(dp[:i]) + i
print(max(dp))
