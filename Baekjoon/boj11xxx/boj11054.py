import sys

read = sys.stdin.readline

seqLen = int(read())
seq = [*map(int, read().split(" "))]
ans = 0
dp_inc = [1 for _ in range(seqLen)]
dp_dec = [1 for _ in range(seqLen)]

for i in range(1, seqLen):
    for j in range(i):
        if seq[i] > seq[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

for i in range(seqLen - 2, -1, -1):
    for j in range(seqLen - 1, i, -1):
        if seq[i] > seq[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

for i in range(seqLen):
    ans = max(ans, dp_dec[i] + dp_inc[i] - 1)

print(ans)
