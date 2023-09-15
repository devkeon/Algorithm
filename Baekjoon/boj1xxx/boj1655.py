import sys
import heapq

read = sys.stdin.readline

n = int(read())
xheap = []
nheap = []
midterm = -10001
for a in range(n):
    k = int(read())
    if midterm <= k:
        heapq.heappush(nheap, k)
    else:
        heapq.heappush(xheap, -k)
    if len(nheap) > len(xheap):
        heapq.heappush(xheap, -heapq.heappop(nheap))
    elif len(xheap) - 2 == len(nheap):
        heapq.heappush(nheap, -heapq.heappop(xheap))
    if a == 0:
        midterm = k
    else:
        midterm = (-xheap[0] + nheap[0]) // 2
    print(-xheap[0])
