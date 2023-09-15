n = int(input())
inum = list(map(int, input().split(" ")))

inum.sort()
ans = 0

for i in range(n):
    left, right = 0, n - 2
    t = inum[:i] + inum[i + 1:]
    while left < right:
        tmp = t[left] + t[right]
        if tmp < inum[i]:
            left += 1
        elif tmp > inum[i]:
            right -= 1
        else:
            ans += 1
            break

print(ans)
