#﻿swex 1961 숫자 배열 회전

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

def clockwise(board):
    tmpBoard = deepcopy(board)
    for r in range(N):
        for c in range(N):
            tmp = board[N-c-1][r]
            answer[r] += str(tmp)
            tmpBoard[r][c] = tmp
        answer[r] += ' '
    return tmpBoard

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    answer = ['' for _ in range(N)]
    for _ in range(3):
        board = clockwise(board)
    print('#%d'%test_case)
    for r in range(N):
        print(answer[r])