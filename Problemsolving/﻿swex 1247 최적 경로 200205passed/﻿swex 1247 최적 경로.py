#﻿swex 1247 최적 경로

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    import sys
    input = sys.stdin.readline
################################
def howLong(start,end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def DFS(start,dist,level):
    if level == N:
        global minDist
        minDist = min(minDist, dist + howLong(start, home))
        return

    for i in range(N):
        if chk[i]:
            continue
        end = clients[i]
        chk[i] = 1
        DFS(end,dist + howLong(start,end),level + 1)
        chk[i] = 0

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    tmp = tuple(map(int,input().split()))
    x = [tmp[i*2:i*2+2] for i in range(N+2)]
    start = x[0]
    home = x[1]
    clients = x[2:]
    chk = [0 for _ in range(N)]
    minDist = 20000
    dist = 0
    DFS(start,dist,0)
    print('#%d'%test_case,minDist)



