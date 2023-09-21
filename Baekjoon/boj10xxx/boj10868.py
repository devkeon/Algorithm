import sys
import math
read = sys.stdin.readline

n, m = map(int, read().split())
seq = []
h = 2**(math.ceil(math.log2(n)) + 1)
minimum = [0 for _ in range(h)]


def init(cur, start, end):
    if start == end:
        minimum[cur] = seq[start]
    else:
        mid = (start + end) // 2
        left = init(cur * 2, start, mid)
        right = init(cur * 2 + 1, mid + 1, end)
        minimum[cur] = min(left, right)
    return minimum[cur]


def find(cur, start, end, left, right):
    if start > right or end < left:
        return 1000000001
    if left <= start and end <= right:
        return minimum[cur]
    mid = (start + end) // 2
    l_min = find(cur * 2, start, mid, left, right)
    r_min = find(cur * 2 + 1, mid + 1, end, left, right)
    return min(l_min, r_min)


for _ in range(n):
    seq.append(int(read()))
init(1, 0, n - 1)
for _ in range(m):
    u, v = map(int, read().split())
    print(find(1, 0, n - 1, u - 1, v - 1))

