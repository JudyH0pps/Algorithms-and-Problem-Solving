# ﻿swex 4871 그래프 경로

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

from collections import defaultdict


def DFS(now, end):
    if end == now:
        global find
        find = True
        return
    visit[now] = 1
    for next in graph[now]:
        if visit[next]:
            continue
        DFS(next, end)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())
    visit = [0] * (V + 1)
    find = False
    DFS(S, G)
    if find:
        print('#%d' % test_case, 1)
    else:
        print('#%d' % test_case, 0)
