#﻿swex 2105 모의 SW 디저트 카페

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
    print()
def isWall(row,col):
    if 0 <= row < N and 0 <= col < N:
        return False
    return True

#5시, 8시, 11시, 1시
dr = [1,1,-1,-1]
dc = [1,-1,-1,1]
def travel(startr, startc, row, col, dir, path, level, start, dirSet):
    for ndir in range(4):
        if ndir in dirSet or ndir == ((dir + 2)%4):
            continue
        nr = row + dr[ndir]
        nc = col + dc[ndir]
        if not start and nr == startr and startc == nc:
            global maxLevel
            maxLevel = max(maxLevel, level+1)
            return

        #print('from',row,col,'to',nr,nc,'방향',dir,'->',ndir)
        if isWall(nr,nc):
            continue
        now = board[nr][nc]
        if now in path:
            continue

        ndirSet = deepcopy(dirSet)
        if dir != ndir:
            ndirSet.append(dir)
            #print('방향전환',ndirSet)
        npath = deepcopy(path)
        npath.append(board[nr][nc])
        travel(startr,startc,nr,nc,ndir,npath,level+1,False, ndirSet)

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    maxLevel = -1
    for r in range(N):
        for c in range(N):

            if (r,c) == (0,0) or (r,c) == (0,N-1) or (r,c) == (N-1,0) or (r,c) == (N-1,N-1):
                continue
            now = board[r][c]
            path = list()
            path.append(now)
            travel(startr = r, startc = c, row = r, col = c, dir = 0, path = path, level = 0, start = True, dirSet = list())

    print('#%d'%test_case,maxLevel)
