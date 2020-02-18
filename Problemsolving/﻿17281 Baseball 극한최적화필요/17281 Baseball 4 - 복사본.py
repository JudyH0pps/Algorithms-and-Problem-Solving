#﻿17281 Baseball

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
from collections import deque
from copy import deepcopy

def action(tasun):
    board, outs, scores, inning = 0,0,0,0
    i = 0
    while True:
        if i == 3:
            taza = 0
        elif i >= 4:
            taza = tasun[i-1]
        else:
            taza = tasun[i]

        perform = results[inning][taza]

        if perform == 0:
            outs += 1
            if outs >= 3:
                # print('이닝끝')
                outs = 0
                inning += 1
                board = 0
                if inning >= N:
                    break
        else:
            board += 1
            for _ in range(perform):
                board <<= 1
                if board >= 8:
                    scores += 1
                    board -= 8

        i = (i+1)%9
    global maxScore
    maxScore = max(maxScore,scores)

def permutations(level):

    if level == M:
        action(nums)
    for i in range(level,M):
        nums[i],nums[level] = nums[level],nums[i]
        permutations(level+1)
        nums[i], nums[level] = nums[level], nums[i]



N = int(input())
# 0 아웃, 1 안타, 2 2루타, 3 3루타, 4 홈런
results = [list(map(int,input().split())) for _ in range(N)]
nums = list(range(1,9))
M = len(nums)
chk = [0] * M

maxScore = -1
permutations(0)
print(maxScore)


