#﻿16985 Maaaaaaaaaze

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

from collections import deque

def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()
    print()

N = 5
# 0 벽 1 이동가능 칸

boards = [[list(map(int,input().split())) for _ in range(N)] for _ in range(N)]

printB(boards[0])
printB(x)

