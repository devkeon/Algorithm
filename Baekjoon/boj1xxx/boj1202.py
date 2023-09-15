import sys
import heapq

read = sys.stdin.readline

n, k = map(int, read().split(" "))
heap = []
for i in range(n):
    heapq.heappush(heap, list(map(int, read().split(" "))))
knapsack = [int(read()) for _ in range(k)]
knapsack.sort()
ans = 0
can = []

for maximum in knapsack:
    while heap and heap[0][0] <= maximum:
        heapq.heappush(can, -heapq.heappop(heap)[1])
    if can:
        ans -= heapq.heappop(can)

print(ans)
