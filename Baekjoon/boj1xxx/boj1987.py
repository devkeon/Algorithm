import sys

read = sys.stdin.readline
visit = [False for _ in range(26)]
r, c = map(int, read().split())
alphabet = [list(read().rstrip()) for _ in range(r)]
start = ord(alphabet[0][0]) - 65
visit[start] = True
mr = [0, 1, 0, -1]
mc = [1, 0, -1, 0]
ans = 0


def dfs(row, col, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nr = row + mr[i]
        nc = col + mc[i]
        if 0 <= nr < r and 0 <= nc < c:
            asci = ord(alphabet[nr][nc]) - 65
            if not visit[asci]:
                visit[asci] = True
                dfs(nr, nc, cnt + 1)
                visit[asci] = False


dfs(0, 0, 1)
print(ans)
