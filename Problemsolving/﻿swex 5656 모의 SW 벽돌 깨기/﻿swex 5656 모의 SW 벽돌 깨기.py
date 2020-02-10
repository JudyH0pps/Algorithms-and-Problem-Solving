#﻿swex 5656 모의 SW 벽돌 깨기

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
from copy import deepcopy

def printB(board):
    for i in range(H):
        for j in range(W):
            print(board[i][j],end=' ')
        print()

def isWall(row, col):
    if 0<= row < H and 0 <= col < W:
        return False
    return True

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def blockBreak(start):
    def findTop(start):
        for row in range(H):
            now = board[row][start]
            if now:
                return row, now

    def doBreak(row,col):
        now = tmpBoard[row][col]
        if not now:
            return
        tmpBoard[row][col] = 0
        for dir in range(4):
            nr, nc = row, col
            for _ in range(now):
                nr += dr[dir]
                nc += dr[dir]
                if isWall(nr, nc):
                    break
                doBreak(nr,nc)

    toprow, top= findTop(start)
    if top == 1:
        return 1
    topcol = start
    tmpBoard = deepcopy(board)
    doBreak(toprow,topcol)
    printB(tmpBoard)


T = int(input())

for test_case in range(1,T+1):
    N, W, H = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(H)]

    cumulSum = 0
    for r in range(H):
        cumulSum += sum(board[r])
    #printB(board)

    maxBreakd = -1
    for i in range(W):
        breaked = blockBreak(i)

