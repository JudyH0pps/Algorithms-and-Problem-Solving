#﻿swex 5650 모의 SW 핀볼 게임

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

T = int(input())
for test_case in range(1,T+1):
    N = int(input())

    board = [list(map(int,input().split())) for _ in range(N)]
