import sys

read = sys.stdin.readline
n, s = map(int, read().split(" "))
seq = list(map(int, read().split(" ")))
ans = 100001
left, right, ssum = 0, 1, seq[0]

while left < right:
    if ssum < s:
        if right < n:
            right += 1
            ssum += seq[right - 1]
        else:
            break
    else:
        ans = min(right - left, ans)
        ssum -= seq[left]
        left += 1

print(ans if ans != 100001 else 0)
