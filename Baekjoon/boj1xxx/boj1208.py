import sys
read = sys.stdin.readline

n, s = map(int, read().split())
seq = [*map(int, read().split())]
seq.sort()
mid = n // 2
left_seq = {}
ans = 0


def leftcomb(cur, subsum):
    if cur == mid:
        if subsum in left_seq.keys():
            left_seq[subsum] += 1
        else:
            left_seq[subsum] = 1
        return
    leftcomb(cur + 1, subsum)
    leftcomb(cur + 1, subsum + seq[cur])


def rightcomb(cur, subsum):
    if cur == n:
        global ans
        if s - subsum in left_seq.keys():
            ans += left_seq[s - subsum]
        return
    rightcomb(cur + 1, subsum)
    rightcomb(cur + 1, subsum + seq[cur])


leftcomb(0, 0)
rightcomb(mid, 0)
print(ans if s != 0 else ans - 1)
