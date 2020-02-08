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
from copy import deepcopy
import sys
sys.setrecursionlimit(10 ** 6)

def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


def printCube(cube):
    for i in range(N):
        printB(cube[i])
    print('---------')


# 시계방향으로 회전
def spin(board, num):
    before = deepcopy(board)
    for _ in range(num):
        nboard = [[0 for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                nboard[r][c] = before[N - c - 1][r]
        before = nboard
    return nboard


def everySpin(now, level):
    if level == 4:
        print(now)
        return
    for i in range(4):
        nnow = now[:]
        nnow.append(i)
        everySpin(nnow, level + 1)


# 내가 짠 높이 순열
'''
chk = [0 for _ in range(5)]
def everyTotem(now, level):
    if level == 4:
        print(now)
        return
    for i in range(5):
        if chk[i]:
            continue
        nnow = now[:]
        nnow.append(i)
        chk[i] = 1
        everyTotem(nnow,level+1)
        chk[i] = 0

'''


# 수업 시간에 배운거
def everyTotem(depth):
    if depth == 5:
        printCube(cube)
        # 현재 큐브에서 BFS시작하기

        ######
        return

    for i in range(depth, 5):
        cube[i], cube[depth] = cube[depth], cube[i]
        everyTotem(depth + 1)
        cube[i], cube[depth] = cube[depth], cube[i]


N = 5
#################################### Main ##################################

# 0 벽 1 이동가능 칸

cube = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
everyTotem(0)

