import sys
import math

read = sys.stdin.readline

n, m = map(int, read().split())
h = 2**(math.ceil(math.log2(n)) + 1) - 1
seq = [int(read()) for _ in range(n)]
max_tree = [0 for _ in range(h)]
min_tree = [0 for _ in range(h)]


def init(start, end, cur):
    if start == end:
        max_tree[cur] = seq[start]
        min_tree[cur] = seq[start]
    else:
        half = (start + end) // 2
        l_max, l_min = init(start, half, cur * 2)
        r_max, r_min = init(half + 1, end, cur * 2 + 1)
        max_tree[cur] = max(l_max, r_max)
        min_tree[cur] = min(l_min, r_min)
    return [max_tree[cur], min_tree[cur]]


def find(start, end, left, right, cur):
    if start > right or end < left:
        return [-1, 1000000001]
    elif left <= start and end <= right:
        return [max_tree[cur], min_tree[cur]]
    half = (start + end) // 2
    l_max, l_min = find(start, half, left, right, cur * 2)
    r_max, r_min = find(half + 1, end, left, right, cur * 2 + 1)
    return [max(l_max, r_max), min(l_min, r_min)]


init(0, n - 1, 1)
for _ in range(m):
    u, v = map(int, read().split())
    x, y = find(0, n - 1, u - 1, v - 1, 1)
    print(y, x)
