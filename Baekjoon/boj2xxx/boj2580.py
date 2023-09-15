import sys

read = sys.stdin.readline

board = [list(map(int, read().split(" "))) for _ in range(9)]
need = []


def sqcheck(row, col):
    used = [0 for _ in range(10)]
    able = []
    rs = row // 3 * 3
    cs = col // 3 * 3
    for i in range(3):
        for j in range(3):
            used[board[rs + i][cs + j]] = 1

    for i in range(9):
        used[board[row][i]] = 1
        used[board[i][col]] = 1

    for i in range(1, 10):
        if used[i] == 0:
            able.append(i)

    return able


def fill(row, col, idx):
    can = sqcheck(row, col)
    global board, need
    if not can:
        return
    for num in can:
        board[row][col] = num
        if idx + 1 == len(need):
            for k in range(9):
                for a in range(9):
                    print(board[k][a], end=" ")
                print()
            exit(0)
        else:
            fill(need[idx + 1][0], need[idx + 1][1], idx + 1)
        board[row][col] = 0


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            need.append([i, j])

fill(need[0][0], need[0][1], 0)
