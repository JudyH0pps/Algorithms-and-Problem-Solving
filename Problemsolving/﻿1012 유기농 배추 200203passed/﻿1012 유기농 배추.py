# ﻿1012 유기농 배추

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = f.readline
################################
from copy import deepcopy

def printB():
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()
    print()

# 동 남 서 북
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def DFS(y,x):
    board[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M or chk[ny][nx]:
            continue
        if board[ny][nx]:
            chk[ny][nx] = 1
            DFS(ny,nx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    chk = deepcopy(board)

    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            chk[i][j] = 1
            if not board[i][j]:
                continue
            cnt += 1
            DFS(i,j)

    print(cnt)
