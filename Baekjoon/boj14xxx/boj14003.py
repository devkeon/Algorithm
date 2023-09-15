import sys
from bisect import bisect_left
read = sys.stdin.readline

n = int(read())
seq = [*map(int, read().split())]
subseq = [seq[0]]
cnt = 1
ind = [[seq[0], 1]]

for i in range(1, n):
    if seq[i] > subseq[-1]:
        subseq.append(seq[i])
        cnt += 1
        ind.append([seq[i], cnt])
    else:
        left = bisect_left(subseq, seq[i])
        if subseq[left] > seq[i]:
            subseq[left] = seq[i]
            ind.append([seq[i], left + 1])

ans = []
for i in range(len(ind) - 1, -1, -1):
    if ind[i][1] == cnt:
        ans.append(ind[i][0])
        cnt -= 1
print(len(ans))
print(*ans[::-1])

# input:
# 16
# -60 -41 -100 8 -8 -52 -62 -61 -76 -52 -52 14 -11 -2 -54 46
# answer:
# 7
# -100 -62 -61 -52 -11 -2 46
