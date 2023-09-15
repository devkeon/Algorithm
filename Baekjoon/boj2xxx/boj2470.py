import sys

read = sys.stdin.readline

n = int(read())
ans = [0, 1]
liq = list(map(int, read().split(" ")))
liq.sort()

base, limit = 0, n - 1
s = 2000000000

while base < limit:
    tmp = liq[base] + liq[limit]
    if abs(tmp) < s:
        ans[0], ans[1] = base, limit
        s = abs(tmp)
        if s == 0:
            break
    if tmp > 0:
        limit -= 1
    else:
        base += 1

print(liq[ans[0]], liq[ans[1]])
