import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
island = [[*map(int, read().split())] for _ in range(n)]
border = []
mr = [0, 1, 0, -1]
mc = [1, 0, -1, 0]
visit = [[False for _ in range(n)] for j in range(n)]


def find_border(row, col, inum):
    dq = deque()
    dq.append([row, col])
    while dq:
        cr, cc = dq.pop()
        for i in range(4):
            nr = cr + mr[i]
            nc = cc + mc[i]
            if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
                if island[nr][nc] == 1:
                    dq.append([nr, nc])
                    visit[nr][nc] = True
                else:
                    if [cr, cc] not in border[inum]:
                        border[inum].append([cr, cc])


num = -1
for i in range(n):
    for j in range(n):
        if island[i][j] == 1 and not visit[i][j]:
            num += 1
            border.append([])
            find_border(i, j, num)
ans = 10001
for i in range(num + 1):
    for j in range(i + 1, num + 1):
        for x, y in border[i]:
            for a, b in border[j]:
                ans = min(ans, abs(x - a) + abs(y - b) - 1)
print(ans)
