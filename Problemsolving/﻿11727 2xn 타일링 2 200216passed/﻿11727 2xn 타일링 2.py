#﻿11727 2xn 타일링 2

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

n = int(input())

dp = [1] * (n+1)
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-2]

print(dp[n]%10007)
