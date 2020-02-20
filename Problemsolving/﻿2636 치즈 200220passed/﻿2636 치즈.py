#﻿2636 치즈

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
sys.setrecursionlimit(10**6)

def printB(board):
    for i in range(N):
        for j in range(M):
            print(board[i][j],end=' ')
        print()

delta = (
    (0,1),
    (1,0),
    (-1,0),
    (0,-1)
)
def DFS(row,col):

    for i in range(4):
        dr,dc = delta[i]
        nr = row + dr
        nc = col + dc
        if not ( 0 <= nr < N and 0 <= nc < M) or board[nr][nc] == 9 or board[nr][nc] == 8:
            continue
        if board[nr][nc] == 1:
            board[nr][nc] = 8
            continue
        else:
            board[nr][nc] = 9
        DFS(nr,nc)

N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

time = 0
cnt = 0
while True:
    DFS(0,0)
    before = cnt
    cnt = 0
    for r in range(N):
        for c in range(M):
            now = board[r][c]
            if now == 9:
                board[r][c] = 0
            if now == 8:
                board[r][c] =0
                cnt += 1
    if cnt == 0:
        break
    time += 1
    # printB(board)
print(time)
print(before)