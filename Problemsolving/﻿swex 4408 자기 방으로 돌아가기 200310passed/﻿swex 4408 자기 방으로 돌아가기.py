# ﻿swex 4408 자기 방으로 돌아가기

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
for tc in range(1, T + 1):
    N = int(input())
    students = [tuple(map(int, input().split())) for _ in range(N)]

    rouka = [0] * 201

    for s, e in students:
        if s > e:
            M = s
            m = e
        else:
            M = e
            m = s

        rouka[(m - 1) // 2] += 1
        rouka[(M - 1) // 2 + 1] -= 1

    maxN = rouka[0]
    for i in range(1, 201):
        rouka[i] += rouka[i - 1]
        if rouka[i] > maxN:
            maxN = rouka[i]

    print("#%d" % tc, maxN)
