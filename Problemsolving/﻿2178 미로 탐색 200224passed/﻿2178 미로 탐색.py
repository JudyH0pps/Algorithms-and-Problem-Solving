#﻿2178 미로 탐색

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
    (0,1),
    (1,0),
    (-1,0),
    (0,-1)
)
def BFS(row,col,level):
    q = deque()
    visit[row][col] = level + 1
    q.append((row,col,level+1))
    while q:
        row,col,level = q.popleft()
        for i in range(4):
            dr,dc = delta[i]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] and not visit[nr][nc]:
                visit[nr][nc] = level + 1
                q.append((nr,nc,level+1))



N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
BFS(0,0,0)
print(visit[-1][-1])