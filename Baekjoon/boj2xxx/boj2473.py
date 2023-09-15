n = int(input())

liq = [*map(int, input().split())]
liq.sort()
ans = [0, 0, 0]
summ = 3000000001
for i in range(n):
    one = liq[i]
    s, e = 0, len(liq) - 2
    while s < e:
        if s == i:
            s += 1
            continue
        elif e == i:
            e -= 1
            continue
        tmp = one + liq[s] + liq[e]
        if abs(tmp) < summ:
            summ = abs(tmp)
            ans[0] = liq[s]
            ans[1] = liq[e]
            ans[2] = one

            if summ == 0:
                break
        if tmp < 0:
            s += 1
        else:
            e -= 1

print(*sorted(ans))
