#﻿swex 2112 보호 필름

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    import sys
    input = sys.stdin.readline
################################

moji = ['A','B']
def printB():
    for i in range(D):
        for j in range(W):
            print(moji[board[i][j]],end=' ')
        print()
    print()

from collections import deque

def gumsa(board,changed):
    for col in range(W):
        if changed[col]:
            continue
        before = board[0][col]
        cnt = 1
        for row in range(1, D):
            now = board[row][col]
            if now == before:
                cnt += 1
                if cnt >= K:
                    OK[col] = 1
                    break
            else:
                cnt = 1
            before = now

T = int(input())

for test_case in range(1,T+1):
    D,W,K = map(int,input().split())
    # A = 0, B = 1
    board = [list(map(int,input().split())) for _ in range(D)]
    changed = [0 for _ in range(W)]
    OK = [0 for _ in range(W)]

    q = deque()
    q.append(([],-1))

    before_leng = -1
    perm = []
    while q:
        now,last = q.popleft()
        leng = len(now)
        if leng and before_leng != leng:
            perm = []
            for i in range(1<<leng):
                x = '%s'%bin(i)[2:].zfill(leng)
                perm.append(x)
            before_leng = leng
        ###
        # 하나의 부분집합을 구했음 - > 약품 투입해서 검사
        ###





        ###
        for i in range(last+1,D):
            nnow = now[:]
            nnow.append(i)
            q.append((nnow,i))