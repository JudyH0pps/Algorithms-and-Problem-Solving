import sys

sys.stdin = open('5251.txt')


#5251 최소 이동 거리
T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    length = [float('inf')] * (N + 1)
    visit = [0] * (N + 1)
    length[0] = 0

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        if s == 0:
            length[e] = w

    now = -1
    while now != N:
        minl = float('inf')
        mini = -1
        for i in range(1, N + 1):
            if not visit[i] and minl > length[i]:
                minl = length[i]
                mini = i

        now = mini
        visit[now] = 1

        for candidate in range(1, N + 1):
            if graph[now][candidate] and not visit[candidate]:
                if length[candidate] > length[now] + graph[now][candidate]:
                    length[candidate] = length[now] + graph[now][candidate]

    print('#%d' % tc, length[N])
