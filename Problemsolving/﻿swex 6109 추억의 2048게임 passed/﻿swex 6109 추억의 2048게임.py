#﻿swex 6109 추억의 2048게임

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
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()

def Clockwise(board, n):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    nboard = deepcopy(board)
    for _ in range(n):
        for i in range(N):
            for j in range(N):
                tmp[i][j] = nboard[N-j-1][i]
        nboard = deepcopy(tmp)
    return nboard

def jungli(line):
    i = 0
    for _ in range(N-1):
        if line[i] == 0:
            line.pop(i)
            line.append(0)
        else:
            i += 1

    for i in range(N - 1):
        first = line[i]
        if first == line[i+1]:
            line = line[:i] + line[i+1:N] + [0]
            line[i] = first*2

    #print(line)
    return line

spin = {'up':3, 'down':1, 'right':2, 'left':0}

T = int(input())

for test_case in range(1,T+1):
    N, move = input().split()
    N = int(N)
    board = [list(map(int,input().split())) for _ in range(N)]
    board = Clockwise(board,spin[move])
    #print('clockwise')
    #printB(board)
    for r in range(N):
        now = board[r]
        #print(now)
        board[r] = jungli(now)
    board = Clockwise(board,4 - spin[move])
    print('#%d'%test_case)
    printB(board)


