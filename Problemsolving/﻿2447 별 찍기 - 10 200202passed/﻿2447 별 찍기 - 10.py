#﻿2447 별 찍기 - 10

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################
def printB(board):
    for i in range(N):
        for j in range(N):
            print('%1s'%board[i][j],end='')
        print()
    print()

def star(row,col,N):
    if N == 1:
        lines[row][col] = '*'
        return
    next = N//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(row + i*next, col + j * next,next)

N = int(input())
lines = [['' for _ in range(N)] for _ in range(N)]
star(0,0,N)
printB(lines)

