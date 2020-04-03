from collections import deque, defaultdict

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = defaultdict(int)

    S, G = map(int, input().split())

    def BFS(S, G):
        q = deque()
        q.append((S, 0))
        while q:
            now, level = q.popleft()
            for nextnode in graph[now]:
                if nextnode == G:
                    return level + 1
                if visit[nextnode]:
                    continue
                visit[nextnode] = 1
                q.append((nextnode, level + 1))
        return 0

    print("#%d" % tc, BFS(S, G))
