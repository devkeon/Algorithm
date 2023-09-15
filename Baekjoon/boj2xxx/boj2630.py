import sys

read = sys.stdin.readline

n = int(read())
paper = [[*map(int, read().split())] for _ in range(n)]
ans = [0, 0]


def check(width, r, c):     # check node if it is leaf node
    w, b = 0, 0
    for i in range(r, r + width):
        for j in range(c, c + width):
            if paper[i][j] == 0:
                w += 1
            else:
                b += 1
    return w, b


def tree(row, col, height):     # tree (recursive definition)
    white, blue = check(height, row, col)
    if white > 0 and blue > 0:
        nh = height // 2
        nr = row + nh
        nc = col + nh
        tree(row, col, nh)
        tree(nr, col, nh)
        tree(row, nc, nh)
        tree(nr, nc, nh)
    else:
        if blue == 0:
            ans[0] += 1
        else:
            ans[1] += 1


tree(0, 0, n)
print(*ans, sep='\n')

