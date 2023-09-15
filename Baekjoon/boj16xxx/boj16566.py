import sys

read = sys.stdin.readline

n, m, k = map(int, read().split())
mcard = [*map(int, read().split())]
chulsu = [*map(int, read().split())]
mcard.sort()
minsu = []
root = [int(i) for i in range(m)]


def bs(target):
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        if mcard[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    xroot = find(x)
    yroot = find(y)
    root[xroot] = yroot


for chul in chulsu:
    ind = bs(chul)
    rfind = find(ind)
    minsu.append(mcard[rfind])
    if rfind < m - 1:
        union(rfind, rfind + 1)

for card in minsu:
    print(card)
