import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

papers = [[*map(int, read().split())] for _ in range(10)]
remain = [0, 5, 5, 5, 5, 5]
ans = 101


def check(row, col, k):
    for i in range(k):
        for j in range(k):
            if papers[row + i][col + j] == 0:
                return False
    return True


def backtracking(cr, cc, cnt):
    if cr >= 10:
        global ans
        ans = min(ans, cnt)
        return
    if cc >= 10:
        backtracking(cr + 1, 0, cnt)
        return
    if papers[cr][cc] == 1:
        for i in range(5, 0, -1):
            if remain[i] == 0:
                continue
            nr, nc = cr + i - 1, cc + i - 1
            if nr >= 10 or nc >= 10:
                continue
            if not check(cr, cc, i):
                continue
            for a in range(i):
                for b in range(i):
                    papers[cr + a][cc + b] = 0
            remain[i] -= 1
            backtracking(cr, nc + 1, cnt + 1)
            for a in range(i):
                for b in range(i):
                    papers[cr + a][cc + b] = 1
            remain[i] += 1
    else:
        backtracking(cr, cc + 1, cnt)


backtracking(0, 0, 0)
print(ans if ans != 101 else -1)
