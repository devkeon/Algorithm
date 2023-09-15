import sys

read = sys.stdin.readline

n, slope = map(int, read().split(" "))

road = [list(map(int, read().split(" "))) for _ in range(n)]


def check(line):
    used = [False for _ in range(n)]
    for i in range(n - 1):
        if abs(line[i] - line[i + 1]) > 1:
            return False
        if line[i] < line[i + 1]:
            for h in range(slope):
                if i - h < 0 or line[i] != line[i - h] or used[i - h]:
                    return False
                else:
                    used[i - h] = True
        elif line[i] > line[i + 1]:
            for h in range(1, slope + 1):
                if i + h >= n or line[i + 1] != line[i + h] or used[i + h]:
                    return False
                else:
                    used[i + h] = True
    return True


ans = 0
for x in range(n):
    use = [False for _ in range(n)]
    if check([road[x][k] for k in range(n)]):
        ans += 1
    if check([road[k][x] for k in range(n)]):
        ans += 1

print(ans)
