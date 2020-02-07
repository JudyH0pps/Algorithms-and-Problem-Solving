#﻿swex 1979 어디에 단어가 들어갈 수 있을까

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

moji = ['■','□']
def printB():
    for i in range(N):
        for j in range(N):
            print(moji[board[i][j]],end=' ')
        print()
    print()

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    words = 0

    #가로세기
    for r in range(N):
        ren = False
        cnt = 0
        for c in range(N):
            if board[r][c]:
                cnt += 1
            else:
                if cnt == K:
                    #print(r, c)
                    words += 1
                cnt = 0
        if cnt == K:
            #print(r, c)
            words += 1
    #세로세기
    for c in range(N):
        cnt = 0
        for r in range(N):
            if board[r][c]:
                cnt += 1
            else:
                if cnt == K:
                    #print(r, c)
                    words += 1
                cnt = 0
        if cnt == K:
            #print(r,c)
            words += 1
    #print('K',K)
    #printB()
    print('#%d'%tc,words)


