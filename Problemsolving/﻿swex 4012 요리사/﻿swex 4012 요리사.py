# ﻿swex 4012 요리사

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


def combination(last, level, score):
    for i in range(last + 1, N):
        nscore = score
        for member in team[:level]:
            nscore += board[i][member] + board[member][i]

        if level == N // 2 - 1:
            # print(team,score)
            scores.append(nscore)
            continue

        team[level] = i
        combination(i, level + 1, nscore)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    scores = []
    team = [0] * (N // 2)
    combination(-1, 0, 0)
    minDiff = float('inf')
    for i in range(len(scores) // 2):
        minDiff = min(minDiff, abs(scores[i] - scores[-(i + 1)]))
    print('#%d' % test_case, minDiff)
