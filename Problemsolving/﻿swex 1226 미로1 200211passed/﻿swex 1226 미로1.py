#﻿swex 1226 미로1

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
dr = [0,0,1,-1]
dc = [1,-1,0,0]
def DFS(row,col):
    global find
    if find:
        return
    board[row][col] = 1
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if not (0 <= nr < 16 and 0 <= nc < 16):
            continue
        next = board[nr][nc]
        if next == 3:
            find = True
            return
        elif next == 1:
            continue
        DFS(nr,nc)

for _ in range(10):
    test_case = int(input())
    board = [list(map(int,input())) for _ in range(16)]
    find = False
    DFS(1,1)
    print('#%d'%test_case,end=' ')
    if find:
        print(1)
    else:
        print(0)