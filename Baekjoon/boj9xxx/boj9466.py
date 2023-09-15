import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

t = int(read())


def dfs(ind):
    global result
    visit[ind] = True
    nxt = project[ind] - 1
    cycle.append(ind)
    if visit[nxt]:
        if nxt in cycle:
            result += cycle[cycle.index(nxt):]
            return
    else:
        dfs(nxt)


for i in range(t):
    n = int(read())
    project = [*map(int, read().split(" "))]
    visit = [False for _ in range(n)]
    result = []
    for j in range(n):
        if not visit[j]:
            cycle = []
            dfs(j)
    print(n - len(result))
