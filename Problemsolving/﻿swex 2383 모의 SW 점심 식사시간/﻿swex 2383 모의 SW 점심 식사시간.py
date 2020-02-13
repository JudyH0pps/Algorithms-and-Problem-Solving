#﻿swex 2383 모의 SW 점심 식사시간

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

def printB():
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()
    print()

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

