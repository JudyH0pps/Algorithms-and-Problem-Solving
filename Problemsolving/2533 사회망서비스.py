import sys
sys.stdin = open('input.txt')

answer = 0
N = int(input())
graph = {}
cnt = {}
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, [])
    graph[a].append(b)
    cnt[a] = cnt.get(a, 0) + 1
    graph[b] = graph.get(b, [])
    graph[b].append(a)
    cnt[b] = cnt.get(b, 0) + 1

visit = [0] * (N + 1)

levels = {}

stack = [[0, 1]]
visit[1] = 1

while stack:
    level, node = stack.pop()
    levels[level] = levels.get(level, [])
    levels[level].append(node)
    for nextNode in graph[node]:
        if visit[nextNode]:
            continue
        visit[nextNode] = 1
        stack.append([level + 1, nextNode])

maxLevel = len(levels.keys()) - 1

answer = 0
for level in range(maxLevel, -1, -1):
    for node in levels[level]:
        if cnt[node] == 0:
            continue
        for nextNode in graph[node]:
            if cnt[nextNode]:
                break
        else:
            continue
        answer += 1
        for parent in graph[nextNode]:
            if cnt[parent] == 0:
                continue
            cnt[parent] -= 1
        cnt[nextNode] = 0

print(answer)
