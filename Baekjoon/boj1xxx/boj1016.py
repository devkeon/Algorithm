import math

x, y = map(int, input().split())

nono = [False for _ in range(y - x + 1)]
ans = y - x + 1
for i in range(2, int(math.sqrt(y)) + 1):
    square = i**2
    start = x

    for j in range(start, y + 1, square):
        if not nono[j - x]:
            nono[j - x] = True
            ans -= 1
print(ans)
