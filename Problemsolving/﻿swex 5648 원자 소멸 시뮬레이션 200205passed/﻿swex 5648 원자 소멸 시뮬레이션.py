#﻿swex 5648 원자 소멸 시뮬레이션

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

from collections import defaultdict

#상 하 좌 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    Es = [list(map(int,input().split())) for _ in range(N)]
    Es = [[x*2,y*2,dir,K] for x,y,dir,K in Es]
    Ksum = 0
    for _ in range(4004):
        dict = defaultdict(list)
        for i,e in enumerate(Es):
            x,y,dir,K = e
            x += dx[dir]
            y += dy[dir]
            dict[x,y].append(i)
            Es[i] = (x,y,dir,K)

        for key,val in dict.items():
            if len(val) >= 2:
                for i in reversed(val):
                    _,_,_,K = Es.pop(i)
                    Ksum += K

        #print(Es)

    print('#%d'%test_case,Ksum)