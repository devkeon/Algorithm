import sys
sys.setrecursionlimit(10**8)

read = sys.stdin.readline
n, m = map(int, read().split(" "))
board = [list(read().rstrip()) for _ in range(n)]
ans = 11
mr = [1, 0, -1, 0]      # down, right, up, left
mc = [0, 1, 0, -1]
red, blue = [], []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red.extend([i, j])
            board[i][j] = '0'
        if board[i][j] == 'B':
            blue.extend([i, j])
            board[i][j] = '0'


def backtracking(cnt, move, curred, curblue):
    if cnt >= 10:
        return
    nr = mr[move]
    nc = mc[move]
    nrr, ncr = curred
    nrb, ncb = curblue
    while board[nrb + nr][ncb + nc] != '#' and board[nrb + nr][ncb + nc] != 'O':
        nrb += nr
        ncb += nc
    if board[nrb + nr][ncb + nc] == 'O':
        return
    while board[nrr + nr][ncr + nc] != '#' and board[nrr + nr][ncr + nc] != 'O':
        nrr += nr
        ncr += nc
    if board[nrr + nr][ncr + nc] == 'O':
        global ans
        ans = min(ans, cnt + 1)
        return
    if nrr == nrb and ncr == ncb:
        reddis = abs(nrr - curred[0] + ncr - curred[1])
        bluedis = abs(nrb + ncb - curblue[0] - curblue[1])
        if reddis > bluedis:
            nrr -= nr
            ncr -= nc
        else:
            nrb -= nr
            ncb -= nc
    for i in range(4):
        if i == move:
            continue
        backtracking(cnt + 1, i, [nrr, ncr], [nrb, ncb])


for d in range(4):
    backtracking(0, d, red, blue)


print(ans if ans != 11 else -1)
