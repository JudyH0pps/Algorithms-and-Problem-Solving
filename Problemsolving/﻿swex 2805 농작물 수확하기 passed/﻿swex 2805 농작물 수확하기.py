# ﻿swex 2805 농작물 수확하기

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

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    cumul = 0
    left = N // 2; right = left
    for i in range(N//2+1):
        for c in range(left, right + 1):
            cumul += board[i][c]
        left -= 1; right += 1
    left += 1;
    right -= 1
    for i in range(N//2+1,N):
        left += 1;
        right -= 1
        for c in range(left,right+1):
            cumul += board[i][c]

    print('#%d'%test_case,cumul)
