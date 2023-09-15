import sys

read = sys.stdin.readline

n = int(read())
board = [[*map(int, read().split(" "))] for _ in range(n)]
mr = [-1, 1, 0, 0]
mc = [0, 0, 1, -1]
ans = 0


def dfs(cnt, direction, before):
    if cnt == 5:
        global ans
        m = 0
        for i in range(n):
            for j in range(n):
                m = max(m, before[i][j])
        ans = max(ans, m)
        return
    nxt = [[0 for _ in range(n)] for k in range(n)]
    visit = [[False for a in range(n)] for b in range(n)]
    if direction == 0:
        for j in range(n):
            for i in range(n):
                num = before[i][j]
                if num > 0:
                    nr = i
                    while nr - 1 >= 0 and nxt[nr - 1][j] == 0:
                        nr += mr[direction]
                    if nr > 0 and num == nxt[nr - 1][j] and not visit[nr - 1][j]:
                        nr += mr[direction]
                        num += num
                        visit[nr][j] = True
                    nxt[nr][j] = num
    elif direction == 1:
        for j in range(n):
            for i in range(n - 1, -1, -1):
                num = before[i][j]
                if num > 0:
                    nr = i
                    while nr + 1 <= n - 1 and nxt[nr + 1][j] == 0:
                        nr += mr[direction]
                    if nr < n - 1 and num == nxt[nr + 1][j] and not visit[nr + 1][j]:
                        nr += mr[direction]
                        num += num
                        visit[nr][j] = True
                    nxt[nr][j] = num
    elif direction == 2:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                num = before[i][j]
                if num > 0:
                    nc = j
                    while nc + 1 <= n - 1 and nxt[i][nc + 1] == 0:
                        nc += mc[direction]
                    if nc < n - 1 and num == nxt[i][nc + 1] and not visit[i][nc + 1]:
                        nc += mc[direction]
                        num += num
                        visit[i][nc] = True
                    nxt[i][nc] = num
    else:
        for i in range(n):
            for j in range(n):
                num = before[i][j]
                if num > 0:
                    nc = j
                    while nc - 1 >= 0 and nxt[i][nc - 1] == 0:
                        nc += mc[direction]
                    if nc > 0 and num == nxt[i][nc - 1] and not visit[i][nc - 1]:
                        nc += mc[direction]
                        num += num
                        visit[i][nc] = True
                    nxt[i][nc] = num
    for i in range(4):
        dfs(cnt + 1, i, nxt)


for h in range(4):
    dfs(0, h, board)

print(ans)
