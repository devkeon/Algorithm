import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split(" "))
board = [list(read().rstrip()) for _ in range(n)]
red, blue = [], []
ans = 11
mr = [1, 0, -1, 0]      # down, right, up, left
mc = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red.extend([i, j])
            board[i][j] = '0'
        if board[i][j] == 'B':
            blue.extend([i, j])
            board[i][j] = '0'


def another(redloc, blueloc):
    dq = deque()
    for i in range(4):
        dq.append([redloc, blueloc, 0, i])
    while dq:
        curred, curblue, cnt, direction = dq.pop()
        if cnt >= 10:
            continue
        nr = mr[direction]
        nc = mc[direction]
        nrr, ncr = curred
        nrb, ncb = curblue
        while board[nrb + nr][ncb + nc] != 'O' and board[nrb + nr][ncb + nc] != '#':
            nrb += nr
            ncb += nc
        if board[nrb + nr][ncb + nc] == 'O':
            continue
        while board[nrr + nr][ncr + nc] != 'O' and board[nrr + nr][ncr + nc] != '#':
            nrr += nr
            ncr += nc
        if board[nrr + nr][ncr + nc] == 'O':
            global ans
            ans = min(ans, cnt + 1)
            continue
        if nrr == nrb and ncr == ncb:
            reddis = abs(nrr - curred[0] + ncr - curred[1])
            bluedis = abs(nrb + ncb - curblue[0] - curblue[1])
            if reddis > bluedis:
                nrr -= nr
                ncr -= nc
            else:
                nrb -= nr
                ncb -= nc
        for j in range(4):
            if j == direction:
                continue
            dq.append([[nrr, ncr], [nrb, ncb], cnt + 1, j])


another(red, blue)
print(ans if ans != 11 else -1)
