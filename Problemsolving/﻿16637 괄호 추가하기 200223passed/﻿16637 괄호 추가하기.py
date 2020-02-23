# ﻿16637 괄호 추가하기

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

def eval(a,op,b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b

N = int(input())
expression = input()
dp = [-2**31] * (N - N//2)
ngdp = [1]*len(dp)
dp[0] = int(expression[0])
if dp[0] < 0:
    ngdp[0] = dp[0]
if len(expression) == 1:
    print(int(expression))
else:
    dp[1] = eval(expression[0],expression[1],expression[2])
    if dp[1] < 0:
        ngdp[1] = dp[1]
    for i in range(2,len(dp)):
        index = 2*i - 1
        right = expression[index+1]
        op = expression[index]
        left = expression[index-1]
        leftOp = expression[index-2]

        a = eval(dp[i-1],op,right)
        b = eval(left,op,right)
        b = eval(dp[i-2],leftOp,b)

        # print(a,b)

        dp[i] = max(a,b)
        ng = min(a,b)
        if ng <= 0:
            ngdp[i] = ng

        if ngdp[i-1] < 1:
            a = eval(ngdp[i-1],op,right)
        if ngdp[i-2] < 1:
            b = eval(left, op, right)
            b = eval(ngdp[i - 2], leftOp, b)
        # print(a,b)
        dp[i] = max(dp[i],a,b)
        ng = min(a,b)
        if ng <= 0:
            ngdp[i] = min(ngdp[i],ng)

        # print(dp)
        # print(ngdp)

    print(dp[-1])