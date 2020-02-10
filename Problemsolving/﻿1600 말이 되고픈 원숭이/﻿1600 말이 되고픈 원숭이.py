# ﻿1600 말이 되고픈 원숭이

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
from itertools import product

def printB(board):
    for i in range(H):
        for j in range(W):
            print(boadr[i][j],end=' ')
        print()

def isWall(row, col):
    if 0 <= row < H and 0 <= col < W:
            return False
    return True

# 동, 서, 남, 북, 1시,2시,4시,5시,7시,8시,10시,11시
dr = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
def move(row, col, dir):
    return row + dr[dir], col + dc[dir]

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]
chk = [[[0] * W for _ in range(H)] for _ in range(K+1)]

q = deque()

find = False
row, col, level, jump = 0, 0, 1, 0
q.append((row, col, level, jump))
while not find and q:
    row,col,level,jump = q.popleft()

    if jump >= K:
        end = 4
    else:
        end = 12

    for i in range(end):
        nr, nc = move(row,col,i)
        if i >= 4:
            j = 1
        else:
            j = 0
        if isWall(nr, nc) or board[nr][nc] or chk[jump+j][nr][nc]:
            continue
        if (nr, nc) == (H-1, W-1):
            answer = level
            find = True
            break
        chk[jump + j][nr][nc] = level+1
        q.append((nr,nc,level+1,jump + j))

if find:
    print(answer)
else:
    print(-1)








