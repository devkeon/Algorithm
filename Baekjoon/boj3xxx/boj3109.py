import sys
read = sys.stdin.readline
r, c = map(int, read().split())
graph = [list(read()) for _ in range(r)]
mr = [-1, 0, 1]
mc = [1, 1, 1]


def dfs(row, col):
    if col == c - 1:
        return 1
    for k in range(3):
        nr = row + mr[k]
        nc = col + mc[k]
        if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] != 'x' and not visit[nr][nc]:
            visit[nr][nc] = True
            tmp = dfs(nr, nc)
            if tmp == 1:
                return tmp
    return 0


visit = [[False for _ in range(c)] for j in range(r)]
ans = 0
for i in range(r):
    visit[i][0] = True
    ans += dfs(i, 0)
print(ans)
