n = int(input())

num = [0 for _ in range(n + 1)]
pn = []
ans = 0

for i in range(2, n + 1):
    if num[i] == 0:
        for j in range(2 * i, n + 1, i):
            num[j] = 1
        pn.append(i)

start, end = 0, 1

while start <= end:
    if end == len(pn) + 1:
        break
    now = sum(pn[start:end])
    if now == n:
        ans += 1
        end += 1
    elif now < n:
        end += 1
    else:
        start += 1

print(ans)

