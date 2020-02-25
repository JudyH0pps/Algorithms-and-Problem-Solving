# ﻿11723 집합

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

SET = 0
M = int(input())
for _ in range(M):
    tmp = input().split()
    if len(tmp) == 2:
        x = int(tmp[1])-1

    if tmp[0] == 'add':
        SET |=  1 << x
    elif tmp[0] == 'remove':
        SET &= ~(1 << x)
    elif tmp[0] == 'check':
        if SET & 1 << x:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        SET ^= 1 << x
    elif tmp[0] == 'all':
        SET = (1 << 21) - 1
    else:
        SET = 0
    # print(tmp[0],x+1,bin(SET))
