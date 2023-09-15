import sys
read = sys.stdin.readline

n, m, h = map(int, read().split())
ladder = [[0 for _ in range(n - 1)] for i in range(h)]
ans = 271
for _ in range(m):
    a, b = map(int, read().split())
    ladder[a - 1][b - 1] = 1


def check():
    for i in range(n):
        now = i
        for a in range(h):
            if now + 1 < n and ladder[a][now] == 1:
                now += 1
            elif now - 1 >= 0 and ladder[a][now - 1] == 1:
                now -= 1
        if now != i:
            break
    else:
        return True
    return False


def backtracking(height, cur, cnt):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(height, h):
        k = cur if i == height else 0
        for j in range(k, n - 1):
            if ladder[i][j] == 0:
                ladder[i][j] = 1
                backtracking(i, j + 2, cnt + 1)
                ladder[i][j] = 0


backtracking(0, 0, 0)
print(ans if ans <= 3 else -1)
