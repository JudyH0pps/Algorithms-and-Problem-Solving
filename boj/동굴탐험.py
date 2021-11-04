from collections import deque


def solution(n, path, order):
    lock = [0] * n
    key = [-1] * n
    visit = [0] * n

    graph = dict()
    for a, b in path:
        graph[a] = graph.get(a, [])
        graph[b] = graph.get(b, [])
        graph[a].append(b)
        graph[b].append(a)

    for k, l in order:
        key[k] = l
        lock[l] = 1

    print(key)
    print(lock)

    q = deque()
    q.append(0)
    visit[0] = 1
    while q:
        print(q)
        node = q.popleft()
        if lock[node]:
            q.append(node)
            continue
        if key[node] >= 0:
            lock[key[node]] = 0
        for nextNode in graph[node]:
            if visit[nextNode]:
                continue
            visit[nextNode] = 1
            q.append(nextNode)

    print(visit)
