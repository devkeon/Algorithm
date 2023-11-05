import sys
read = sys.stdin.readline

h, w = map(int, read().split())
blocks = [*map(int, read().split())]
ans = 0
for i in range(1, w - 1):
    rmax, lmax = blocks[i], blocks[i]
    for j in range(i - 1, -1, -1):
        lmax = max(lmax, blocks[j])
    for j in range(i + 1, w):
        rmax = max(rmax, blocks[j])
    minn = min(rmax, lmax)
    if minn != -1:
        ans += (min(rmax, lmax) - blocks[i])
print(ans)
