import sys
read = sys.stdin.readline

my = [0, -1, 0, 1]
mx = [1, 0, -1, 0]

n = int(read())
square = [[False for _ in range(101)] for _ in range(101)]


def rangecheck(r, c):
    global square
    if 0 <= r <= 100 and 0 <= c <= 100:
        square[r][c] = True
        return
    square[r][c] = False


def dragon_curve(x, y, direction, gen):
    cnt = 1
    direct = [direction]
    x += mx[direction]
    y += my[direction]
    rangecheck(y, x)
    while cnt != 2**gen:
        for a in range(len(direct) - 1, -1, -1):
            nxt = (direct[a] + 1) % 4
            x += mx[nxt]
            y += my[nxt]
            rangecheck(y, x)
            direct.append(nxt)
            cnt += 1


for _ in range(n):
    x, y, d, g = map(int, read().split())
    rangecheck(y, x)
    dragon_curve(x, y, d, g)

tr = [0, 1, 1]
tc = [1, 0, 1]
ans = 0
for i in range(100):
    for j in range(100):
        if square[i][j]:
            for k in range(3):
                if not square[i + tr[k]][j + tc[k]]:
                    break
            else:
                ans += 1
print(ans)
