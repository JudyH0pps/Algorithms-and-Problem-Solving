# ﻿swex 2112 보호 필름

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = f.readline
else:
    import sys

    input = sys.stdin.readline
################################
from collections import deque
from itertools import product


def gumsa(chosen, e):
    tmp = []
    for i in range(len(chosen)):
        tmp.append(board[chosen[i]][:])
        board[chosen[i]] = [e[i]] * W

    result = True
    for c in range(W):
        before = -1
        cnt = 0
        for r in range(D):
            if board[r][c] != before:
                before = board[r][c]
                cnt = 1
            else:
                cnt += 1
            if cnt >= K:
                break
        else:
            result = False
            break

    for i in range(len(chosen)):
        board[chosen[i]] = tmp[i]

    return result


T = int(input())

for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    def BFS():
        q = deque()
        q.append(([], -1))
        while q:
            chosen, last = q.popleft()
            for e in product(range(2), repeat=len(chosen)):
                if gumsa(chosen, e):
                    return len(chosen)
                # print(board)

            for i in range(last + 1, D):
                choose = chosen[:]
                choose.append(i)
                q.append((choose, i))


    print('#%d' % test_case, BFS())