import sys
from collections import deque
read = sys.stdin.readline

r, c, t = map(int, read().split(" "))
p = []
mr = [-1, 0, 1, 0]
mc = [0, 1, 0, -1]
house = [[*map(int, read().split(" "))] for _ in range(r)]
ans = 0
for i in range(r):
    for j in range(c):
        if house[i][j] == -1:
            p.append(i)
        if house[i][j] > 0:
            ans += house[i][j]


def diffusion():
    global house
    change = []
    for i in range(r):
        for j in range(c):
            if house[i][j] > 0:
                spread = house[i][j] // 5
                cnt = 0
                for nxt in range(4):
                    nr = i + mr[nxt]
                    nc = j + mc[nxt]
                    if 0 <= nr < r and 0 <= nc < c and house[nr][nc] > -1:
                        cnt += 1
                        change.append([nr, nc, spread])
                change.append([i, j, -1 * cnt * spread])
    for row, col, plus in change:
        house[row][col] += plus


def wind(loc):
    global house, ans
    antic = loc[0]
    clock = loc[1]
    dq = deque()
    dq.append(0)
    for i in range(1, c):   # ->
        shift = dq.popleft()
        dq.append(house[antic][i])
        house[antic][i] = shift
    for i in range(antic - 1, -1, -1):   # ^
        shift = dq.popleft()
        dq.append(house[i][c - 1])
        house[i][c - 1] = shift
    for i in range(c - 2, -1, -1):   # <-
        shift = dq.popleft()
        dq.append(house[0][i])
        house[0][i] = shift
    for i in range(1, antic):   # down
        shift = dq.popleft()
        dq.append(house[i][0])
        house[i][0] = shift
    ans -= dq.popleft()

    dq.append(0)
    for i in range(1, c):   # ->
        shift = dq.popleft()
        dq.append(house[clock][i])
        house[clock][i] = shift
    for i in range(clock + 1, r):   # down
        shift = dq.popleft()
        dq.append(house[i][c - 1])
        house[i][c - 1] = shift
    for i in range(c - 2, -1, -1):   # <-
        shift = dq.popleft()
        dq.append(house[r - 1][i])
        house[r - 1][i] = shift
    for i in range(r - 2, clock, -1):   # ->
        shift = dq.popleft()
        dq.append(house[i][0])
        house[i][0] = shift
    ans -= dq.popleft()


for _ in range(t):
    diffusion()
    wind(p)
print(ans)
