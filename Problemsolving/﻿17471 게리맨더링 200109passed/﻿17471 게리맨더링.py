#﻿17471 게리맨더링

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################
graph = {}

def regionDivde(start):
    global nowpop
    nowpop += popul[start]
    for near in graph[start+1]:
        next = near - 1
        if visit[next]:
            continue
        if chosen[next] == party:
            visit[next] = 1
            regionDivde(next)

N = int(input())
popul = list(map(int,input().split()))
for i in range(1,N+1):
    tmp = [*map(int,input().split())]
    graph[i] = tmp[1:]

minAns = 1000
for i in range(1, (1 << N) - 1):
    chosen = bin(i)[2:].zfill(N)
    region = 0
    visit = [0] * N
    pops = []
    for i in range(N):
        if visit[i]:
            continue
        party = chosen[i]
        visit[i] = 1
        nowpop = 0
        regionDivde(i)
        region += 1
        pops.append(nowpop)
    if region == 2:
        a, b = pops
        minAns = min(minAns,abs(a-b))

if minAns == 1000:
    print(-1)
else:
    print(minAns)