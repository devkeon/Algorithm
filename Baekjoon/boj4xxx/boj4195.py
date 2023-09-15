import sys

read = sys.stdin.readline

t = int(read())


def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parentss, cnt):
    px = find(x, parentss)
    py = find(y, parentss)
    if px > py:
        parentss[px] = py
        cnt[py] += cnt[px]
        print(cnt[py])
    elif px < py:
        parentss[py] = px
        cnt[px] += cnt[py]
        print(cnt[px])
    else:
        print(cnt[px])
    return


for _ in range(t):
    name = {}
    parent = [int(j) for j in range(200001)]
    count = [1 for i in range(200001)]
    f = int(read())
    j = 0
    for i in range(f):
        names = name.keys()
        user1, user2 = read().rstrip().split()
        if user1 not in names:
            name[user1] = j
            j += 1
        if user2 not in names:
            name[user2] = j
            j += 1
        union(name[user1], name[user2], parent, count)
