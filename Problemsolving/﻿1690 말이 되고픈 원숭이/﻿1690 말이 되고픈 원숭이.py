# ﻿1690 말이 되고픈 원숭이

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

def init(board):
    for i,j in product(range(H),range(W)):
        board[i][j] *= 500

def isWall(row, col):
    if 0 <= row < H and 0 <= col < W:
        if board[row][col] == 500:
            return True
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
init(board)
board[0][0] = 1

q = deque()

find = False
row, col, level, jump = 0, 0, 1, 0
q.append((row, col, level, jump))
while not find and q:
    row,col,level,jump = q.popleft()
    #printB(board)
    if jump >= K:
        end = 4
    else:
        end = 12
    for i in range(end):
        nr, nc = move(row,col,i)
        if (nr, nc) == (H-1, W-1):
            answer = level
            find = True
            break
        if isWall(nr, nc):
            continue
        if i >= 4:
            j = 1
        else:
            j = 0
        board[nr][nc] = level+1
        q.append((nr,nc,level+1,jump + j))

if find:
    print(answer)
else:
    print(-1)








