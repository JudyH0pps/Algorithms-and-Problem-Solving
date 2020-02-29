# ﻿swex 4534 트리 흑백 색칠

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


def DFS(node):

    end = True
    whites = 1
    WB = 1
    for next in graph[node]:
        if not visit[next]:
            end = False
            visit[next] = 1
            white, black = DFS(next)
            whites *= white
            WB *= (white + black)
    if end:
        return 1, 1

    return WB, whites


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (N + 1)
    visit[1] = 1
    print('#%d' % test_case, sum(DFS(1)) % 1000000007)
