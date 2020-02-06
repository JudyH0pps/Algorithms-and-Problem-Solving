#﻿swex 2001 파리 퇴치

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

def calcul(row,col):
    #print(row,col)
    cumul = 0
    for r in range(row, row+M):
        if col == 0:
            tmp = 0
        else:
            tmp = board[r][col-1]
        cumul += board[r][col+M-1] - tmp
    return cumul

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(1,N):
            board[i][j] += board[i][j-1]

    maxDie = -1
    for i in range(N-M+1):
        for j in range(N-M+1):
            maxDie = max(calcul(i,j), maxDie)

    print('#%d'%tc,maxDie)

