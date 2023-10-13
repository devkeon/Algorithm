import sys
read = sys.stdin.readline

ans, total = [-1, -1], float('inf')
n = int(read())
liq = [*map(int, read().split())]


def bs(start, end, base):
    back = [float('inf'), -1]
    while start <= end:
        mid = (start + end) // 2
        summ = base + liq[mid]
        if abs(summ) < back[0]:
            back[0] = abs(summ)
            back[1] = liq[mid]
        if summ < 0:
            start = mid + 1
        elif summ > 0:
            end = mid - 1
        else:
            back[0] = abs(summ)
            back[1] = liq[mid]
            break
    return back


for i in range(n - 1):
    arr = bs(i + 1, n - 1, liq[i])
    if total > arr[0]:
        total = arr[0]
        ans = [liq[i], arr[1]]

print(*ans)

