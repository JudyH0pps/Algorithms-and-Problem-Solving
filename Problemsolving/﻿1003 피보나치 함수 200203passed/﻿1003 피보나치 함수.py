#﻿1003 피보나치 함수

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
else:
    import sys
    input = sys.stdin.readline
################################

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0 for _ in range(max(2,N+1))]
    # (0 호출 수 , 1 호출 수)
    dp[0] = (1,0)
    dp[1] = (0,1)

    index = 2
    while index <= N:
        dp[index] = tuple(map(sum,zip(dp[index-1],dp[index-2])))
        index += 1

    print(*dp[N])