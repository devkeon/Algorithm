import sys
from bisect import bisect_left

read = sys.stdin.readline

n = int(read())
seq = [*map(int, read().split())]
subseq = [seq[0]]
for i in range(1, n):
    if subseq[-1] < seq[i]:
        subseq.append(seq[i])
        continue
    left = bisect_left(subseq, seq[i])
    if subseq[left] > seq[i]:
        subseq[left] = seq[i]
print(len(subseq))
