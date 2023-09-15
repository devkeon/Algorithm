import sys

read = sys.stdin.readline

R, C, m = int(read().split())
sharks = []
mr = [-1, 1, 0, 0]
mc = [0, 0, 1, -1]
for _ in range(m):
    r, c, s, d, z = map(int, read().split())
    sharks.append([r - 1, c - 1, s, d - 1, z])


def catch(cur):
    near = R
    for i in range(R):
        shark = sharks[i][1]
        if shark == cur and shark < near:
            near = shark
    if near != R:
        return sharks[near][4]
    else:
        return 0


def change(head):
    if head == 0:
        return 1
    elif head == 1:
        return 0
    elif head == 2:
        return 3
    else:
        return 2


def move():
    for i in range(m):
        row, col, speed, direction = sharks[i][:4]
        rowterm = 2 * R - 2
        if direction == 0:
            
        elif direction == 1:





        else:
            row += nr
        if nc + col >= C:

        else:
            col += nc


for i in range(C):


