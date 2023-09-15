import sys

read = sys.stdin.readline

A = int(read())
seq = list(map(int, read().split(" ")))
lis = [seq[0]]

for i in seq:
    if i > lis[-1]:
        lis.append(i)
    else:
        start, end = 0, len(lis) - 1
        while start <= end:
            mid = (start + end) // 2
            if lis[mid] < i:
                start = mid + 1
            elif lis[mid] > i:
                end = mid - 1
            else:
                break
        if lis[start] > i:
            lis[start] = i
print(len(lis))
