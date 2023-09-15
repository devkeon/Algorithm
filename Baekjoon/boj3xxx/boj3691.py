import sys

read = sys.stdin.readline

t = int(read())
for _ in range(t):
    ans, budget = 10000001, 0
    n, b = map(int, read().split())
    pc, already = [], []
    for i in range(n):
        key, band, price, quality = read().split()
        if key in already:      # pc == 종
            num = already.index(key)
            pc[num].append([int(price), int(quality)])
        else:
            already.append(key)
            pc.append([[int(price), int(quality)]])
    values = []
    for i in range(len(pc)):    # minimum price
        pc[i].sort()
        budget += pc[i][0][0]
        values.append(pc[i][0][1])
        ans = min(ans, pc[i][0][1])

    while budget <= b:      # 부품 하나씩 교환
        ans = min(values)
        category = values.index(ans)
        if not pc[category]:
            break
        qind = 0
        while qind < len(pc[category]) - 1:      # 최솟값 부품 최솟값 벗어날 동안 교체
            budget -= pc[category][qind][0]
            qind += 1
            budget += pc[category][qind][0]
            if budget > b:
                del pc[category][:qind]
                break
            if ans < pc[category][qind][1]:
                ans = pc[category][qind][1]
                values[category] = ans
                del pc[category][:qind]
                break
        else:
            del pc[category][:qind + 1]
    print(ans)
