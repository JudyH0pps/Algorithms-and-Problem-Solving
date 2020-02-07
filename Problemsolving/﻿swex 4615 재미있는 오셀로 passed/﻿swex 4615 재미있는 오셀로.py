#﻿swex 4615 재미있는 오셀로

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

moji = ['.','B','W']
def printB(board):
    for i in range(N):
        for j in range(N):
            print(moji[board[i][j]],end=' ')
        print()
    print()

def cntB(board):
    cntW = 0
    cntB = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cntB +=1
            elif board[i][j] == 2:
                cntW += 1

    return cntB, cntW



T = int(input())

# 북, 북동, 동, 동남, 남, 남서, 서, 북서
dc = [0,1,1,1,0,-1,-1,-1]
dr = [-1,-1,0,1,1,1,0,-1]
dir = ['북', '북동', '동', '동남','남','남서', '서', '북서']
for test_case in range(1,T+1):
    N, M = map(int,input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]
    mid = N//2
    board[mid][mid] = 2
    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    #printB(board)
    for _ in range(M):
        row,col,color = map(int,input().split())
        nowr = row - 1
        nowc = col - 1
        board[nowr][nowc] = color
        #printB(board)
        for i in range(8):
            nextr = nowr + dr[i]
            nextc = nowc + dc[i]
            if not(0<= nextr < N and 0 <= nextc < N):
                continue
            ncolor = board[nextr][nextc]
            #print(nextr,nextc)
            change = False
            if ncolor and ncolor != color:
                #print(dir[i])
                #방향 찾았으니까 이쪽으로 쭉 간다
                cnt = 1
                tmp = []
                while True:
                    gor = nowr + dr[i] * cnt
                    goc = nowc + dc[i] * cnt
                    if not (0<= gor <N and 0<= goc <N):
                        change = False
                        break
                    going = board[gor][goc]
                    if going == 0:
                        change = False
                        break
                    elif going == color:
                        change = True
                        break
                    tmp.append((gor,goc))
                    cnt += 1
            if change:
                for r,c in tmp:
                    board[r][c] = color


    print('#%d'%test_case,*cntB(board))