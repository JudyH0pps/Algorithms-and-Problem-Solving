# ﻿13459 구슬 탈출

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
from collections import deque


def printB(board):
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()
    print()

def stacking(y,left,right):


def move():
    for y in range(N):
        print(y)
        before = '#'
        for x in range(M):
            now = board[y][x]
            if before != now and now != '#':
                q = deque()
                left = x
            elif before != now and now == '#':
                right = x

            before = now


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
move()
