import sys

read = sys.stdin.readline
n = int(read())
eggs = [list(map(int, read().split())) for _ in range(n)]
ans = 0
visit = [False for _ in range(n)]


def remain(arr, now):
    tmp = []
    for i in range(n):
        if arr[i][0] > 0 and i != now:
            tmp.append(i)
    return tmp


def backtracking(cur):
    global ans
    if cur == n:
        cnt = 0
        for i in range(n):
            if eggs[i][0] < 1:
                cnt += 1
        ans = max(ans, cnt)
        return
    if eggs[cur][0] < 1:
        backtracking(cur + 1)
    else:
        remaineggs = remain(eggs, cur)
        if not remaineggs:
            cnt = 0
            for i in range(n):
                if eggs[i][0] < 1:
                    cnt += 1
            ans = max(ans, cnt)
            return
        else:
            for i in remaineggs:
                eggs[i][0] -= eggs[cur][1]
                eggs[cur][0] -= eggs[i][1]
                backtracking(cur + 1)
                eggs[i][0] += eggs[cur][1]
                eggs[cur][0] += eggs[i][1]


backtracking(0)
print(ans)
