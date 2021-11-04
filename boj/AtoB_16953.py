import heapq

def BFS(A, B):
    q = []
    heapq.heappush(q, [0, B])
    while q:
        level, N = heapq.heappop(q)
        if N == A:
            return level + 1
        if N % 10 == 1 and N // 10 >= 1:
            heapq.heappush(q, [level + 1, N // 10])
        elif N % 2 == 0 and N // 2 >= 1:
            heapq.heappush(q, [level + 1, N // 2])
    return -1

A, B = map(int, input().split())
answer = BFS(A, B)
print(answer)

