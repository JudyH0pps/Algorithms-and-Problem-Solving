# ﻿swex 1220 Magnetic

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
def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cumul = 0
    for c in range(N):
        one = False
        two = False
        cnt = 0
        for r in range(N):
            now = board[r][c]
            if now == 1:
                one = True
            elif one and now == 2:
                cnt += 1
                one = False
            # if one and (now == 0 or r == N - 1):
            #     cnt += 1
            #     one = two = False
            # print(r, c, now,one,two,cnt)
        cumul += cnt
    print('#%d' % test_case, cumul)
