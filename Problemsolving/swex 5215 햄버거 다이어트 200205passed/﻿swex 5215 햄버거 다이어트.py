# ﻿swex 5215 햄버거 다이어트

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = f.readline
else:
    import sys

    input = sys.stdin.readline
################################

def DFS(taste, calo,last):
    global max_taste

    for i in range(last,N):
        if chk[i]:
            continue
        now_taste, now_calo = ingres[i]
        next_calo = now_calo + calo
        if next_calo > L:
            #print(taste)
            max_taste = max(max_taste,taste)
            continue
        next_taste = now_taste + taste
        #print(now_taste,now_calo,next_taste,next_calo)
        DFS(next_taste,next_calo,i+1)
    max_taste = max(max_taste, taste)


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    max_taste = -1
    ingres = [tuple(map(int,input().split())) for _ in range(N)]
    chk = [0 for _ in range(N)]
    DFS(0,0,0)
    print('#%d %d'%(test_case,max_taste))

