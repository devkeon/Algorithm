import sys
import math
read = sys.stdin.readline
n, m, k = map(int, read().split())
h = 2**(math.ceil(math.log2(n)) + 1)
seq = [int(read()) for _ in range(n)]
seg = [0 for _ in range(h + 1)]
div = 1000000007


def init(cur, start, end):
    if start == end:
        seg[cur] = seq[start]
    else:
        half = (start + end) // 2
        seg[cur] = (init(cur * 2, start, half) * init(cur * 2 + 1, half + 1, end)) % div
    return seg[cur]


def update(cur, start, end, idx, target):
    if idx < start or idx > end:
        return 1
    if start == end:
        if start == idx:
            seg[cur] = target
        return
    half = (start + end) // 2
    update(cur * 2, start, half, idx, target)
    update(cur * 2 + 1, half + 1, end, idx, target)
    seg[cur] = (seg[cur * 2] * seg[cur * 2 + 1]) % div


def submult(cur, start, end, left, right):
    if left > end or right < start:
        return 1
    elif left <= start and end <= right:
        return seg[cur]
    half = (start + end) // 2
    return (submult(cur * 2, start, half, left, right) * submult(cur * 2 + 1, half + 1, end, left, right)) % div


init(1, 0, n - 1)
for i in range(m + k):
    a, b, c = map(int, read().split())
    if a == 1:
        update(1, 0, n - 1, b - 1, c)
        seq[b - 1] = c
    else:
        print(int(submult(1, 0, n - 1, b - 1, c - 1)))
