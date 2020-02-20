#﻿2589 보물섬

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
from collections import deque

delta = (
    (0,1),#동
    (1,0),#남
    (0,-1),#서
    (-1,0)#북
    )

def BFS(row,col,level):
    # print(row,col,level)
    q = deque()
    q.append((row,col,level))
    maxL = -1
    while q:
        row,col,level= q.popleft()
        # print(row,col,level)
        visit[row][col] = 1
        maxL = max(maxL, level)
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if not(0<= nr < N and 0<=nc<M) or board[nr][nc] == 'W' or visit[nr][nc]:
                continue
            # print('in',nr,nc,level)

            q.append((nr,nc,level+1))

    # print(maxL)

    global maxLevel
    maxLevel = max(maxLevel,maxL)



N, M = map(int,input().split())
board = [list(input()) for _ in range(M)]

maxLevel = -1
for r in range(N):
    for c in range(M):
        if board[r][c] == 'L':
            visit = [[0]*M for _ in range(N)]
            BFS(r,c,0)
            break



print(maxLevel)
