# ﻿swex 1238 contact

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
################################
from collections import defaultdict, deque

for test_case in range(1, 11):
    L, start = map(int, input().split())
    tmp = tuple(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(0, L, 2):
        a, b = tmp[i:i + 2]
        if b not in graph[a]:
            graph[a].append(b)

    visit = defaultdict(int)
    levels = defaultdict(list)
    q = deque()
    q.append((start, 0))
    visit[start] = 1
    levels[0].append(start)
    while q:
        before, level = q.popleft()
        for node in graph[before]:
            if not visit[node]:
                visit[node] = 1
                levels[level + 1].append(node)
                q.append((node, level + 1))
    # print(graph)
    # print(levels)
    print('#%d' % test_case, max(levels[level]))
