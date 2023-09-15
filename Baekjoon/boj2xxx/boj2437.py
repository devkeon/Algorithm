import sys

read = sys.stdin.readline
n = int(read())
weight = [*map(int, read().split())]
weight.sort()
s = 0
for i in range(n):
    if s + 1 >= weight[i]:
        s += weight[i]
    else:
        break
print(s + 1)
