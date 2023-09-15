import sys
from bisect import bisect_left

read = sys.stdin.readline
n = int(read())

a = [*map(int, read().split())]
b = [*map(int, read().split())]
c = [int(i) for i in range(max(a) + 1)]

for i in range(n):
    c[a[i]] = i
for i in range(n):
    b[i] = c[b[i]]

seq = [b[0]]
for i in range(1, n):
    if seq[-1] < b[i]:
        seq.append(b[i])
    else:
        left = bisect_left(seq, b[i])
        if seq[left] > b[i]:
            seq[left] = b[i]
print(len(seq))
