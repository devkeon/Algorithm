import sys
from collections import deque
read = sys.stdin.readline

t = int(read())


def bfs(cur):
    global color, vertex
    dq = deque()
    dq.append(cur)
    color[cur] = 1
    while dq:
        now = dq.popleft()
        for nxt in vertex[now]:
            if color[nxt] == 0:
                dq.append(nxt)
                color[nxt] = color[now] * -1
            elif color[nxt] == color[now]:
                return False
    return True


for _ in range(t):
    V, E = map(int, read().split(" "))
    vertex = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, read().split(" "))
        vertex[u - 1].append(v - 1)
        vertex[v - 1].append(u - 1)
    color = [0 for k in range(V)]
    for i in range(V):
        if color[i] == 0:
            tmp = bfs(i)
            if not tmp:
                print("NO")
                break
    else:
        print("YES")
