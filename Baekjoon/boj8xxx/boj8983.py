import sys
read = sys.stdin.readline

m, n, r = map(int, read().split(" "))
shoot = list(map(int, read().split(" ")))
animal = [list(map(int, read().split(" "))) for _ in range(n)]
shoot.sort()


def bs(ax, ay):
    start, end, cnt = 0, m - 1, 0
    while start <= end:
        mid = (start + end) // 2
        if shoot[mid] < ax - r:
            start = mid + 1
        elif shoot[mid] > ax + r:
            end = mid - 1
        else:
            distance = abs(shoot[mid] - ax) + ay
            if distance <= r:
                cnt += 1
                break
            else:
                tmp = ax - shoot[mid]
                if tmp > 0:
                    start = mid + 1
                else:
                    end = mid - 1
    return cnt


ans = 0
for x, y in animal:
    ans += bs(x, y)

print(ans)
