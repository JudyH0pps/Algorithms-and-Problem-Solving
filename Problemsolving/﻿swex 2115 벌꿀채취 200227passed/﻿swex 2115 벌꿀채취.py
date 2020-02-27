# ﻿swex 2115 벌꿀채취

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
################################
from itertools import combinations


def honey(alist, blist):
    score = 0
    maxPow = -1
    for k in range(len(alist), -1, -1):
        for comb in combinations(alist, k):
            tmp = sum(map(lambda x: x ** 2, comb))
            if sum(comb) <= C and maxPow < tmp:
                maxPow = tmp
                a = comb
    score += maxPow
    maxPow = -1
    for k in range(len(blist), -1, -1):
        for comb in combinations(blist, k):
            tmp = sum(map(lambda x: x ** 2, comb))
            if sum(comb) <= C and maxPow < tmp:
                maxPow = tmp
                b = comb
    score += maxPow

    # print(alist, blist, '->', a, b)

    return score


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    maxScore = -1
    for ar in range(N):
        for ac in range(N - M + 1):
            alist = board[ar][ac:ac + M]
            br = ar
            bc = ac + M
            while br < N:
                while bc < N - M + 1:
                    blist = board[br][bc:bc + M]
                    score = honey(alist, blist)
                    if score > maxScore:
                        maxScore = score
                    bc += 1
                bc = 0
                br += 1

    print('#%d' % test_case, maxScore)
