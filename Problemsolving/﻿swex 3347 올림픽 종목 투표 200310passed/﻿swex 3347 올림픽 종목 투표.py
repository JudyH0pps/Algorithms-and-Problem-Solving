# ﻿swex 3347 올림픽 종목 투표

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
from collections import defaultdict

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    vote = defaultdict(int)
    maxVote = -1
    winner = -1

    for b in B:
        for i, a in enumerate(A):
            if b >= a:
                vote[i + 1] += 1
                if vote[i + 1] > maxVote:
                    maxVote = vote[i + 1]
                    winner = i + 1
                break

    print('#%d' % tc, winner)
