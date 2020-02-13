#﻿2615 오목

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

dr = [1,0,1,-1]
dc = [1,1,0,1]
def DFS(sr,sc,row, col,dir,level,color):
    global find
    if find:
        return
    chk[dir][row][col] = 1
    nr = row + dr[dir]
    nc = col + dc[dir]
    if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color and not chk[dir][nr][nc]:
        DFS(sr,sc,nr,nc,dir,level+1,color)
    else:
        if level == 4:
            print(color)
            print(sr + 1, sc + 1)
            find = True
            return

board = [list(map(int,input().split())) for _ in range(19)]
chk = [[[0]*19 for _ in range(19)] for _ in range(4)]
find = False
for c in range(19):
    for r in range(19):
        now = board[r][c]
        if now:
            for i in range(4):
                if not chk[i][r][c]:
                    chk[i][r][c] = 1
                    DFS(r,c,r,c,i,0,now)
if not find:
    print(0)