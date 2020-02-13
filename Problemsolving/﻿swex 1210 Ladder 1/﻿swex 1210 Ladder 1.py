# ﻿swex 1210 Ladder 1

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()

dr = [0, 0, -1]
dc = [1, -1, 0]
def DFS(row,col,level):
    #print(row,col)
    if row == 0:
        global minLevel, minCol
        if level < minLevel:
            minCol = col
            minLevel = level
        return

    for i in range(3):
        nr = row + dr[i]
        nc = col + dc[i]
        if not (0<=nr<100 and 0<=nc<100) or board[nr][nc] == 0:
            continue
        board[nr][nc] = 0
        DFS(nr,nc,level+1)
        break

for _ in range(10):
    test_case = int(input())
    rowleng = 100
    board = [list(map(int, input().split())) for _ in range(rowleng)]

    minLevel = 10000
    minCol = -1
    for c in range(100):
        if board[99][c] == 2:
            DFS(99,c,0)

    print('#%d'%test_case,minCol)