# ﻿swex 3752 가능한 시험 점수

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
for test_case in range(1, int(input()) + 1):
    int(input())
    scores = sorted(list(map(int, input().split())))
    dp = 1
    for e in scores:
        dp |= dp << e
    print('#%d'%test_case,bin(dp).count('1'))
