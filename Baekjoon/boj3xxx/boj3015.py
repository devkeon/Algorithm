import sys

read = sys.stdin.readline
n = int(read())
lines = [int(read()) for _ in range(n)]
stack = []
ans = 0

for p in lines:
    while stack and stack[-1][0] < p:
        ans += stack.pop()[1]
    if not stack:
        stack.append([p, 1])
        continue
    if stack[-1][0] == p:
        cur = stack.pop()[1]
        ans += cur
        if stack:
            ans += 1
        stack.append([p, cur + 1])
    else:
        stack.append([p, 1])
        ans += 1
print(ans)
