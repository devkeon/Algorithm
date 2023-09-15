from collections import deque

seq = input()
exp = input()
dq = deque()
for i in range(len(seq)):
    dq.append(seq[i])
    if dq[-1] == exp[-1]:
        for j in range(len(exp)):
            if dq[len(dq) - j - 1] != exp[len(exp) - j - 1]:
                break
        else:
            for k in range(len(exp)):
                dq.pop()
ans = "".join(dq)
print(ans if ans else "FRULA")
