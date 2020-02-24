# ﻿11437 LCA

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


def BFS(now):
    visit = [0] * N
    visit[0] = 1
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next - 1]:
                continue
            visit[next - 1] = 1
            parents[next] = now
            q.append(next)


N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

parents = [0] * (N + 1)
parents[1] = 1
BFS(1)
# print(parents)
memo = {}
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if a in memo:
        apath = memo[a]
    else:
        apath = [a]
        ap = a
        while ap != 1:
            ap = parents[ap]
            apath.append(ap)
        memo[a] = apath
    if b in memo:
        bpath = memo[b]
    else:
        bpath = [b]
        bp = b
        while bp != 1:
            bp = parents[bp]
            bpath.append(bp)
        memo[b] = bpath

    if len(bpath) < len(apath):
        short = bpath
        long = apath
    else:
        short = apath
        long = bpath

    for e in short:
        if e in long:
            print(e)
            break
