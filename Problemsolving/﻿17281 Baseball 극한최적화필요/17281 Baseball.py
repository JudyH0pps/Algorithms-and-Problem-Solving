# ﻿17281 Baseball

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
from itertools import permutations


def action(tasun):
    i = 0
    score = 0
    for inning in range(N):
        outs = 0
        b1, b2, b3 = 0, 0, 0
        while outs < 3:
            if results[inning][tasun[i]] == 0:
                outs += 1
            elif results[inning][tasun[i]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif results[inning][tasun[i]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif results[inning][tasun[i]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif results[inning][tasun[i]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            i = (i + 1) % 9
    return score


N = int(input())
# 0 아웃, 1 안타, 2 2루타, 3 3루타, 4 홈런
results = [list(map(int, input().split())) for _ in range(N)]


maxScore = -1
for e in permutations(range(1,9)):
    maxScore = max(maxScore,action(list(e)[:3] + [0] + list(e)[3:]))
print(maxScore)
