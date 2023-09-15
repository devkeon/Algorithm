import sys
import math

read = sys.stdin.readline

n, m, k = map(int, read().split())
seq = [int(read()) for _ in range(n)]
h = math.ceil(math.log2(n))
num = 2 ** (h + 1)
seg = [0] * num


def init(start, end, curnode):
    if start == end:
        seg[curnode] = seq[start]
    else:
        half = (start + end) // 2
        seg[curnode] = init(start, half, curnode * 2) + init(half + 1, end, curnode * 2 + 1)
    return seg[curnode]


def subsum(node, start, end, left, right):
    if right < start or left > end:
        return 0
    elif left <= start and end <= right:
        return seg[node]
    half = (start + end) // 2
    return subsum(node * 2, start, half, left, right) + subsum(node * 2 + 1, half + 1, end, left, right)


def update(node, start, end, diff, idx):
    if idx < start or idx > end:
        return
    seg[node] += diff
    if start != end:
        half = (start + end) // 2
        update(node * 2, start, half, diff, idx)
        update(node * 2 + 1, half + 1, end, diff, idx)


init(0, n - 1, 1)
ans = []
for i in range(m + k):
    a, b, c = map(int, read().split())
    if a == 1:
        update(1, 0, n - 1, c - seq[b - 1], b - 1)
        seq[b - 1] = c
    else:
        ans.append(subsum(1, 0, n - 1, b - 1, c - 1))
for x in ans:
    print(x)

