import sys
sys.setrecursionlimit(10**8)

seq = input()
ans = 4


def backtracking(k, left, right):
    if k > 3:
        return
    if left >= right:
        global ans
        ans = min(ans, k)
        return
    if seq[left] != seq[right]:
        backtracking(k + 1, left + 1, right)
        backtracking(k + 1, left, right - 1)
        backtracking(k + 2, left + 1, right - 1)
    else:
        backtracking(k, left + 1, right - 1)


backtracking(0, 0, len(seq) - 1)
print(ans if ans <= 3 else -1)
