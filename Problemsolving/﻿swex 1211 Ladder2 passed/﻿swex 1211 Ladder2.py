#﻿swex 1211 Ladder2

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

def goDown(start):
    # print(start)
    cnt = 0
    row = 0
    col = start
    # 0 동, 1 서 , 2 남
    beforedir = 2
    while row < N - 1:
        if col <= N-2 and beforedir != 1 and board[row][col+1]:
            col += 1
            beforedir = 0
            # print('동',end=' ')
        elif beforedir != 0 and col > 0 and board[row][col-1]:
            col -= 1
            beforedir = 1
            # print('서',end=' ')
        else:
            # print('남',end=' ')
            row += 1
            beforedir = 2
        cnt += 1
    # print(row,col)
    # print(board[row][col])

    return cnt

N = 100
for _ in range(10):
    test_case = int(input())
    #0 빈칸, 1 사다리, 2 도착지점
    board = [list(map(int,input().split())) for _ in range(N)]
    minDist = 50000
    minStart = -1
    for i in range(N):
        if board[0][i]:
            tmp = goDown(i)
            #print(tmp)
            if tmp <= minDist:
                minDist = tmp
                minStart = i

    print('#%d'%test_case,minStart)


