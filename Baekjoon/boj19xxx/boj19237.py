import sys

read = sys.stdin.readline

n, m, k = map(int, read().split())
sharks = [[] for _ in range(m + 1)]
underWater = [[*map(int, read().split())] for _ in range(n)]        # 상어가 남긴 향 종류 & 현위치
scent = [[0 for i in range(n)] for j in range(n)]       # 상어가 남긴 향 지속시간
for i in range(n):
    for j in range(n):
        if underWater[i][j] != 0:
            num = underWater[i][j]
            sharks[num].append(i)
            sharks[num].append(j)
            scent[i][j] = k
sharkHead = [0]
sharkHead.extend([*map(int, read().split())])
priority = [[] for _ in range(m + 1)]
mr = [0, -1, 1, 0, 0]
mc = [0, 0, 0, -1, 1]

for i in range(1, m + 1):
    for _ in range(4):
        priority[i].append([*map(int, read().split())])
sec = 1001
while sec > 0:
    for i in range(1, m + 1):
        if not sharks[i]:
            continue
        cr, cc = sharks[i][0], sharks[i][1]
        for j in range(4):
            idx = priority[i][sharkHead[i] - 1][j]
            nr, nc = cr + mr[idx], cc + mc[idx]
            if (0 > nr or nr >= n) or (0 > nc or nc >= n):
                continue
            if underWater[nr][nc] == 0 and scent[nr][nc] == 0:
                scent[nr][nc] = k + 1
                sharks[i][0] = nr
                sharks[i][1] = nc
                sharkHead[i] = idx
                break
            elif underWater[nr][nc] == 0 and scent[nr][nc] == k + 1:
                del sharks[i][1]
                del sharks[i][0]
                break
        else:
            for j in range(4):
                idx = priority[i][sharkHead[i] - 1][j]
                nr, nc = cr + mr[idx], cc + mc[idx]
                if (0 > nr or nr >= n) or (0 > nc or nc >= n):
                    continue
                if underWater[nr][nc] == i:
                    scent[nr][nc] = k + 1
                    sharks[i][0] = nr
                    sharks[i][1] = nc
                    sharkHead[i] = idx
                    break
    tmp = 0
    for i in range(1, m + 1):
        if not sharks[i]:
            tmp += 1
            continue
        sr, sc = sharks[i]
        underWater[sr][sc] = i
    for i in range(n):
        for j in range(n):
            if scent[i][j] > 0:
                scent[i][j] -= 1
                if scent[i][j] == 0:
                    underWater[i][j] = 0
    sec -= 1
    if tmp == m - 1:
        break

print(1001 - sec if sec != 0 else -1)
