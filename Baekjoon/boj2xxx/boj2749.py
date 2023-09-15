cycle = 1500000
n = int(input()) % cycle
mem = [0 for i in range(cycle + 1)]
mem[1] = 1
for i in range(2, n + 1):
    mem[i] = (mem[i - 1] + mem[i - 2]) % 1000000
print(mem[n])
