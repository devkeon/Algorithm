import sys
read = sys.stdin.readline

ans, total = [-1, -1], float('inf')
n = int(read())
liq = [*map(int, read().split())]
l, r = 0, n - 1
while l < r:
    summ = liq[l] + liq[r]
    if total > abs(summ):
        total = abs(summ)
        ans[0], ans[1] = liq[l], liq[r]
    if summ < 0:
        l += 1
    elif summ > 0:
        r -= 1
    else:
        break

print(*ans)
