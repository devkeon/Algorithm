import sys
read = sys.stdin.readline

n, s = map(int, read().split())
seq = [*map(int, read().split())]
seq.sort()
mid = n // 2
left, right = seq[:mid], seq[mid:]
left_seq = {}
right_seq = {}
ans = 0


def leftcomb(cur, subsum):
    if cur == mid:
        return
    newsum = subsum + seq[cur]
    if newsum in left_seq.keys():
        left_seq[newsum] += 1
    else:
        left_seq[newsum] = 1
    leftcomb(cur + 1, subsum)
    leftcomb(cur + 1, newsum)


def rightcomb(cur, subsum):
    if cur == n:
        return
    newsum = subsum + seq[cur]
    if newsum in right_seq.keys():
        right_seq[newsum] += 1
    else:
        right_seq[newsum] = 1
    rightcomb(cur + 1, subsum)
    rightcomb(cur + 1, newsum)


leftcomb(0, 0)
rightcomb(mid, 0)
leftkey = list(left_seq.keys())
rightkey = right_seq.keys()
for i in range(len(leftkey)):
    toRight = s - leftkey[i]
    if toRight in rightkey:
        ans += (left_seq[leftkey[i]] * right_seq[toRight])
if s in leftkey:
    ans += left_seq[s]
if s in rightkey:
    ans += right_seq[s]
print(ans)
