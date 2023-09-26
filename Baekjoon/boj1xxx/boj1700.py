import sys
import heapq
read = sys.stdin.readline

n, k = map(int, read().split())
using = [*map(int, read().split())]
usingidx = [101 for _ in range(k)]
for i in range(k):
    for j in range(i + 1, k):
        if using[i] == using[j]:
            usingidx[i] = j
            break
ans = 0
useindex = []
outlet = []
for i in range(k):
    if len(outlet) != n:
        if using[i] not in outlet:
            outlet.append(using[i])
            useindex.append(usingidx[i])
            continue
    if using[i] not in outlet:
        ans += 1
        ind = useindex.index(max(useindex))
        del outlet[ind]
        del useindex[ind]
        outlet.append(using[i])
        useindex.append(usingidx[i])
    else:
        ind = outlet.index(using[i])
        useindex[ind] = usingidx[i]
print(ans)
