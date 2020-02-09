#﻿swex 2814 최장 경로

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
################################
from collections import defaultdict
from time import time

start = time()
inputs = lambda : input().split()

def connect(a,b):
    if a not in graph[b]:
        graph[b].append(a)
    if b not in graph[a]:
        graph[a].append(b)

def travel(level, before):
    for i in graph[before]:
        if i in path:
            continue
        path[level] = i
        travel(level + 1, i)
        path[level] = 0
    global maxLevel
    maxLevel = max(level, maxLevel)

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,inputs())
    graph = defaultdict(list)
    graph[0] = [x for x in range(1,N+1)]
    for _ in range(M):
        a, b = map(int,inputs())
        connect(a,b)
    maxLevel = -1
    path = [0] * N
    travel(level = 0, before = 0)

    print('#%d'%test_case, maxLevel)
end = time()
print(end-start)
