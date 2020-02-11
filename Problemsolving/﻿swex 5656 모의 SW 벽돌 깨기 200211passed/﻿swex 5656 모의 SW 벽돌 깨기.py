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
from collections import deque

def printB(board):
    for i in range(H):
        for j in range(W):
            print(board[i][j],end=' ')
        print()
    print()

def isWall(row, col):
    if 0<= row < H and 0 <= col < W:
        return False
    return True

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def down(board):
    for c in range(W):
        q = deque()
        for r in range(H):
            now = board[r][c]
            if now:
                q.append(now)
            board[r][c] = 0
        for r in range(H-1,-1,-1):
            if not q:
                break
            board[r][c] = q.pop()
    return board

def blockBreak(board, start):
    def findTop(start):
        for row in range(H):
            now = board[row][start]
            if now:
                return row, now
        return -1, 0

    def doBreak(row,col):
        now = tmpBoard[row][col]
        tmpBoard[row][col] = 0
        if not now:
            return
        for dir in range(4):
            nr, nc = row, col
            for _ in range(now-1):
                nr += dr[dir]
                nc += dc[dir]
                if isWall(nr, nc):
                    break
                doBreak(nr,nc)

    toprow, top = findTop(start)
    if toprow == -1:
        return board
    topcol = start
    tmpBoard = deepcopy(board)
    doBreak(toprow,topcol)
    tmpBoard = down(tmpBoard)
    return tmpBoard

def blockCount(board):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                cnt += 1
    return cnt

def breakStart(board, level):
    if level == N:
        left = blockCount(board)
        global minLeft
        if left < minLeft:
            minLeft = left
        return
    for i in range(W):
        after = blockBreak(board, i)
        breakStart(after, level + 1)

breakcnt = 0

T = int(input())
for test_case in range(1,T+1):
    N, W, H = map(int,input().split())
    entire = 0
    board = [0] * H
    for r in range(H):
        now = list(map(int,input().split()))
        board[r] = now

    minLeft = 5000
    breakStart(board, 0)
    print('#%d'%test_case,minLeft)