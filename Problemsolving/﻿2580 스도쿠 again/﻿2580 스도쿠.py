#﻿2580 스도쿠

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
from itertools import product
import sys
sys.setrecursionlimit(10**6)

def printB(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j],end=' ')
        print()
    print()

rStart = [0,3,6]
cStart = [0,3,6]
def sudokuChk(row,col,num):
    if num in board[row]:
        return False
    for r in range(9):
        if num == board[r][col]:
            return False
    # print('찾아라', row, col)
    for r,c in tuple(product(rStart,cStart))[::-1]:
        # print(r,c)
        if r <= row and c <= col:
            # print('ok')
            sqr = r
            sqc = c
            break
    
    for r in range(sqr,sqr+3):
        if num in board[r][sqc:sqc+3]:
            return False
    return True

def DFS(level):
    global find
    row,col = zeros[level]
    if (row,col) == (10,10):
        find = True
        return

    for i in range(1,10):
        if sudokuChk(row,col,i):
            board[row][col] = i
            DFS(level+1)
            if find:
                return

    board[row][col] = 0

board = [list(map(int,input().split())) for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        if not board[i][j]:
            zeros.append((i,j))
zeros.append((10,10))
find = False
DFS(0)
printB(board)

