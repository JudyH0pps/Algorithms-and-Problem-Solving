# ﻿swex 1767 프로세서 연결하기

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
################################
from copy import deepcopy

def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


def findcores(board):
    fix = 0
    cores = []
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                if r == 0 or r == N -1 or c == 0 or c == N-1:
                    fix += 1
                else:
                    cores.append((r, c))
    return fix, cores


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def install(row, col, dir, nboard):
    dr, dc = delta[dir]
    plus = 0
    while 0 <= row + dr < N and 0 <= col + dc < N:
        row += dr
        col += dc
        if nboard[row][col]:
            break
        nboard[row][col] = 1
        plus += 1
    else:
        return plus
    return 0


def DFS(now, last, board, code):
    global maxCores, minCode
    if maxCores < len(now):
        maxCores = len(now)
        minCode = 12*12+1
    if maxCores == len(now) and minCode > code:
        minCode = code

    for i in range(last, len(cores)):
        for dir in range(4):
            nboard = deepcopy(board)
            plus = install(*cores[i], dir, nboard)
            if not plus:
                continue
            # printB(nboard)
            next = now[:]
            next.append(i)
            DFS(next, i + 1, nboard, code + plus)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    fix, cores = findcores(board)
    maxCores = -1
    minCode = 12*12+1
    DFS([], 0, board, 0)
    print('#%d'%test_case,minCode)
