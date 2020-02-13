#﻿swex 1267 작업순서

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################
from collections import defaultdict

def DFS(now):
    print(now,end=' ')
    visit[now-1] = 1
    for next in deces[now]:
        PASS = False
        if visit[next-1]:
            continue
        for parent in parents[next]:
            if not visit[parent-1]:
                PASS = True
                break
        if PASS:
            continue
        DFS(next)

T = 10
for test_case in range(1,T+1):
    print('#%d'%test_case,end=' ')
    V, E = map(int,input().split())
    Es = list(map(int,input().split()))
    parents = defaultdict(list)
    deces = defaultdict(list)
    startlist = [i for i in range(1,V+1)]

    visit = [0] * V
    for i in range(0,E*2,2):
        a, b = Es[i:i+2]
        deces[a].append(b)
        parents[b].append(a)
        if b in startlist:
            startlist.remove(b)
    #print(startlist)
    for start in startlist:
        DFS(start)
    print()