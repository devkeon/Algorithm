n = int(input())
k = int(input())

start, end, ans = 1, n * n, 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, mid // i)
    if cnt >= k:
        end = mid - 1
    elif cnt < k:
        start = mid + 1

print(start)
