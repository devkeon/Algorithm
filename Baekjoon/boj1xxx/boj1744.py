import sys

read = sys.stdin.readline

n = int(read())
seq = [int(read()) for _ in range(n)]
seq.sort()
cind = 0 if seq[-1] > 0 else n
for i in range(n - 1):
    if seq[i] <= 0 < seq[i + 1]:
        cind = i + 1
tmp = []
righti = n - 1
while cind <= righti:
    if righti - 1 >= cind and (seq[righti] * seq[righti - 1]) > (seq[righti] + seq[righti - 1]):
        tmp.append(seq[righti] * seq[righti - 1])
        righti -= 2
    else:
        tmp.append(seq[righti])
        righti -= 1

lefti = 0
while lefti < cind:
    if lefti + 1 < cind and (seq[lefti] * seq[lefti + 1]) > (seq[lefti] + seq[lefti + 1]):
        tmp.append(seq[lefti] * seq[lefti + 1])
        lefti += 2
    else:
        tmp.append(seq[lefti])
        lefti += 1
print(sum(tmp))
