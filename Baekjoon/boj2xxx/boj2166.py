import sys
read = sys.stdin.readline

n = int(read())
coordinate = [[*map(int, read().split())] for _ in range(n)]
ans = 0

for i in range(n - 1):
    x = coordinate[i][0] * coordinate[i + 1][1]
    y = coordinate[i][1] * coordinate[i +1][0]
    ans += (x - y)
ans += (coordinate[n - 1][0] * coordinate[0][1] - coordinate[n - 1][1] * coordinate[0][0])
print(round(abs(ans) / 2, 2))

