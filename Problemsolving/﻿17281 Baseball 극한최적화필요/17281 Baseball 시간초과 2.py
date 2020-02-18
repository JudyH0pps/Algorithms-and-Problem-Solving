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

def action(game,taza):
    board, outs, scores, inning = game
    nboard = deepcopy(board)
    perform = results[inning][taza]
    # print(taza)
    if perform == 0:
        outs += 1
        if outs >= 3:
            # print('이닝끝')
            outs = 0
            inning += 1
            board = 0
            if inning >= N:
                global maxScore
                maxScore = max(maxScore, scores)
                return False
    else:
        first = True
        for _ in range(perform):
            x = nboard.popleft()
            if x:
                scores += 1
            if first:
                nboard.append(1)
                first = False
            else:
                nboard.append(0)
    ngame = (nboard, outs, scores, inning)
    # print(ngame)
    return ngame

def mugenloof(now,game):
    # print(now)
    ngame = game
    i = 0
    while True:
        nngame = action(ngame,now[i])
        if not nngame:
            break
        i = (i+1)%9
        ngame = nngame

def permutations(now, level, game):
    if level == 9:
        # print('now',now)
        # print('game',game)
        mugenloof(now,game)

    if level == 3:
        taza = 0
        ngame = action(game,taza)
        if not ngame:
            return
        now.append(taza)
        permutations(now, level + 1, ngame)
        return

    for i in range(len(nums)):
        if chk[i]:
            continue

        taza = nums[i]

        ngame = action(game,taza)
        if not ngame:
            continue

        next = now[:]
        next.append(taza)
        chk[i] = 1
        permutations(next,level+1,ngame)
        chk[i] = 0


N = int(input())
# 0 아웃, 1 안타, 2 2루타, 3 3루타, 4 홈런
results = [list(map(int,input().split())) for _ in range(N)]
nums = list(range(1,9))
chk = [0] * len(nums)
board = [0,0,0]

maxScore = -1
permutations([],0,[deque(board),0,0,0])
print(maxScore)

