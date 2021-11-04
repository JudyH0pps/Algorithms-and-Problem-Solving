import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, input().split())

visit = [0] * 100001

queue = deque()
queue.append([0, N])
visit[N] = 1
while queue:
    time, n = queue.popleft()
    if n == K:
        print(time)
        break
    if n + 1 < 100001 and not visit[n + 1]:
        visit[n + 1] = 1
        queue.append([time + 1, n + 1])
    if n - 1 >= 0 and not visit[n - 1]:
        visit[n - 1] = 1
        queue.append([time + 1, n - 1])
    if n * 2 < 100001 and not visit[n * 2]:
        visit[n * 2] = 1
        queue.append([time + 1, n * 2])
