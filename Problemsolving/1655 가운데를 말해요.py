import sys
import heapq
# sys.stdin = open('input.txt')
input = sys.stdin.readline
N = int(input())

maxheap = []
minheap = []

for _ in range(N):
    a = int(input())
    if minheap and minheap[0] < a:
        heapq.heappush(minheap, a)
    else:
        heapq.heappush(maxheap, -a)

    while not (1 >= len(maxheap) - len(minheap) >= 0):
        if len(maxheap) > len(minheap):
            heapq.heappush(minheap, -heapq.heappop(maxheap))
        else:
            heapq.heappush(maxheap, -heapq.heappop(minheap))

    print(-maxheap[0])
