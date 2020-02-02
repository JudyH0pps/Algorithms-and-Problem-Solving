#﻿swex 1926 간단한 369게임

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################

N = int(input())

for i in range(1,N+1):
    now = i
    clap = 0
    while now:
        if now % 10 and now % 10 % 3 == 0:
            clap += 1
        now //= 10

    if clap:
        print('-'*clap,end=' ')
    else:
        print(i,end=' ')
