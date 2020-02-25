# ﻿14889 스타트와 링크

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

def pick(current, membernum, last, synergy):
    if membernum == N // 2:
        scores.append(synergy)
        return

    for i in range(last + 1, N):
        ncurrent = current[:]
        ncurrent.append(i)
        cumul = 0
        for e in current:
            cumul += board[e][i] + board[i][e]
        pick(ncurrent, membernum + 1, i, synergy + cumul)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
entire = sum(map(sum, board))
scores = []
pick([], 0, -1, 0)

mindiff = 20*20*100
for i in range(len(scores)//2):
    diff = abs(scores[i] - scores[-(i+1)])
    mindiff = min(mindiff,diff)

print(mindiff)
