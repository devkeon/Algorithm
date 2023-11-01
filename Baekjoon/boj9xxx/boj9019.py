import sys
from collections import deque
read = sys.stdin.readline

strarr = "DLRS"
t = int(read())
for _ in range(t):
    dq = deque()
    f, t = map(int, read().split())
    dq.append([f, ""])
    visit = [False for j in range(10001)]
    visit[f] = True
    while dq:
        cur, seq = dq.popleft()
        d = cur * 2 % 10000
        s = cur - 1 if cur - 1 >= 0 else 9999
        l = (cur * 10) % 10000 + (cur * 10) // 10000
        r = (cur // 10) + (cur % 10) * 1000
        numarr = [d, l, r, s]
        for i in range(4):
            if numarr[i] == t:
                print(seq + strarr[i])
                break
        else:
            for i in range(4):
                if not visit[numarr[i]]:
                    visit[numarr[i]] = True
                    dq.append([numarr[i], seq + strarr[i]])
            continue
        break
