import sys

read = sys.stdin.readline

n, c = map(int, read().split(" "))
house = [int(read()) for _ in range(n)]
house.sort()
ans = 1


def bs(start):
    global ans
    end = house[-1] - house[0]
    while start <= end:
        mid = (start + end) // 2
        now = house[0]
        cnt = 1
        for i in range(n):
            if house[i] - now >= mid:
                cnt += 1
                now = house[i]
        if cnt >= c:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1


bs(1)

print(ans)
