from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[0]*N for _ in range(N)]
    visit = [0]*N
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a][b] = 1
        graph[b][a] = 1

    q = deque()
    q.append((0, 0))
    visit[0] = 1
    while q:
        num, level = q.popleft()
        if level == 2:
            break
        for i in range(N):
            if graph[num][i] and not visit[i]:
                visit[i] = 1
                q.append((i, level+1))

    print('#%d'%tc, sum(visit)-1)



