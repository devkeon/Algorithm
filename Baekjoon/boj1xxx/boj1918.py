from collections import deque

exp = list(input())
dic = {'-': 1, '+': 1, '*': 2, '/': 2, '(': 0}
dq = deque()
ans = ''

for now in exp:
    if now == '(':
        dq.append(now)
    elif now == ')':
        while dq and dq[-1] != '(':
            ans += dq.pop()
        dq.pop()
    elif now == '*' or now == '/' or now == '+' or now == '-':
        while dq and dic[dq[-1]] >= dic[now]:
            ans += dq.pop()
        dq.append(now)
    else:
        ans += now
while dq:
    ans += dq.pop()
print(ans)
