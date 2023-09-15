import sys
from collections import deque

read = sys.stdin.readline

m, n, h = map(int, read().split())

tomato = [[[*map(int, read().split())] for a in range(n)] for _ in range(h)]
ripe = []
cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                ripe.append([i, j, k])
                cnt += 1
            elif tomato[i][j][k] == -1:
                cnt += 1
mp = [0, 0, 0, 0, 1, -1]
mr = [1, 0, -1, 0, 0, 0]
mc = [0, 1, 0, -1, 0, 0]


def ripen(ripee):
    new_ripe = []
    for p, r, c in ripee:
        for i in range(6):
            np, nr, nc = p + mp[i], r + mr[i], c + mc[i]
            if 0 <= np < h and 0 <= nr < n and 0 <= nc < m:
                if tomato[np][nr][nc] == 0:
                    new_ripe.append([np, nr, nc])
                    tomato[np][nr][nc] += 1
    return new_ripe


ans = 0
while True:
    ripe = ripen(ripe)
    if ripe:
        cnt += len(ripe)
        ans += 1
    else:
        break

if cnt != n * m * h:
    print(-1)
else:
    print(ans)
