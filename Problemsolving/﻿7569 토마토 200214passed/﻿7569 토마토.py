#﻿7569 토마토

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
from itertools import product

#동서남북상하
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
M,N,H = map(int,input().split())
cube = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
rotten = deque()
def rottenChk(board):
    exe = False
    for x,y,z in product(range(M),range(N),range(H)):
        now = board[z][y][x]
        if now == 1:
            board[z][y][x] = -1
            rotten.append((z,y,x,0))
        elif not exe and now == 0:
            exe = True
    return exe

if not rottenChk(cube):
    print(0)
else:
    def isWall(z,y,x):
        if 0 <= z < H and 0 <= y <N and 0 <= x <M:
            return False
        return True

    while rotten:
        z,y,x,t = rotten.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if not isWall(nz,ny,nx) and cube[nz][ny][nx] == 0:
                cube[nz][ny][nx] = -1
                rotten.append((nz,ny,nx,t+1))

    for x, y, z in product(range(M), range(N), range(H)):
        if cube[z][y][x] == 0:
            print(-1)
            break
    else:
        print(t)



