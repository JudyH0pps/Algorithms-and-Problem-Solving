#﻿swex 4869 종이붙이기

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
    dp = [0] * 1000
    dp[1] = 1
    dp[2] = 3
    for i in range(3,N//10+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    print('#%d'%test_case,dp[N//10])