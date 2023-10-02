import sys
from collections import deque
read = sys.stdin.readline

T = int(read())
mr = [0, 1, 0, -1]
mc = [1, 0, -1, 0]


def simulate(graph, start, firstkey, row, col):
    global memo
    ans = 0
    getting = firstkey
    dq = deque()
    for r, c in start:
        visit[r][c] = True
        dq.append([r, c])
    while dq:
        cr, cc = dq.pop()
        for j in range(4):
            nr, nc = cr + mr[j], cc + mc[j]
            if 0 <= nr < row and 0 <= nc < col and not visit[nr][nc]:
                visit[nr][nc] = True
                if graph[nr][nc].isupper():
                    if graph[nr][nc].lower() in getting:
                        dq.append([nr, nc])
                    else:
                        memo.append([graph[nr][nc], nr, nc])
                elif graph[nr][nc].islower():
                    for door, y, x in memo:
                        if door.lower() == graph[nr][nc]:
                            dq.append([y, x])
                    if graph[nr][nc] not in getting:
                        getting.append(graph[nr][nc])
                    dq.append([nr, nc])
                elif graph[nr][nc] == '$':
                    ans += 1
                    dq.append([nr, nc])
                elif graph[nr][nc] == '.':
                    dq.append([nr, nc])
    return ans


def setfirst(ii, jj):
    global cnt, mapp, memo
    for i in ii:
        for j in jj:
            if not visit[i][j]:
                visit[i][j] = True
                if mapp[i][j] == '.':
                    entrance.append([i, j])
                elif mapp[i][j] == '$':
                    entrance.append([i, j])
                    cnt += 1
                elif mapp[i][j].islower():
                    for d, y, x in memo:
                        if d.lower() == mapp[i][j]:
                            entrance.append([y, x])
                    if mapp[i][j] not in keys:
                        keys.append(mapp[i][j])
                    entrance.append([i, j])
                elif mapp[i][j].isupper():
                    if mapp[i][j].lower() in keys:
                        entrance.append([i, j])
                    else:
                        memo.append([mapp[i][j], i, j])


for _ in range(T):
    h, w = map(int, read().split())
    mapp = [list(read().rstrip()) for _ in range(h)]
    keys = list(read().rstrip())
    visit = [[False for _ in range(w)] for k in range(h)]
    entrance, memo = [], []
    cnt = 0
    setfirst(list(range(h)), [0, w - 1])
    setfirst([0, h - 1], list(range(w)))
    print(simulate(mapp, entrance, keys, h, w) + cnt)
