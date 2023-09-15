import sys

read = sys.stdin.readline

seqLen = int(read())
seq = [*map(int, read().split(" "))]

dp = [1 for _ in range(seqLen)]

for i in range(1, seqLen):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
