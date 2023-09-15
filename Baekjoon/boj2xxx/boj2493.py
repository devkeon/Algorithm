n = int(input())
tower = [*map(int, input().split())]
stack = [[tower[-1], n - 1]]
ans = [0 for _ in range(n)]
for i in range(n - 2, -1, -1):
    while stack and tower[i] >= stack[-1][0]:
        ans[stack[-1][1]] = i + 1
        del stack[-1]
    stack.append([tower[i], i])
print(*ans)
