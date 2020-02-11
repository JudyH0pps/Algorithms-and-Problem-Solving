#﻿swex 1258 행렬찾기

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
def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()
    print()

def isWall(row,col):
    if 0 <= row < N and 0 <= col < N:
        return False
    return True

dr = [0,1,-1,0]
dc = [1,0,0,-1]
def DFS(sr,sc,row,col):
    board[row][col] = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if isWall(nr,nc) or board[nr][nc] == 0:
            continue
        if row == sr and i == 0:
            global garo
            garo += 1
            #print(nr,nc,'가로')
        if col == sc + garo and i == 1:
            global sero
            sero += 1
            # print(nr,nc,'세로')
        DFS(sr,sc,nr,nc)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    # printB(board)

    arrays = []
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                garo = 0
                sero = 0
                DFS(r,c,r,c)
                tmp = (sero+1,garo+1)
                arrays.append(tmp)
                # printB(board)
                # print(tmp)

    arrays.sort(key = lambda a : (a[0]*a[1],a[0]))
    print('#%d'%test_case,len(arrays),end =' ')
    for a in arrays:
        x, y = a
        print(x,y,end=' ')
    print()