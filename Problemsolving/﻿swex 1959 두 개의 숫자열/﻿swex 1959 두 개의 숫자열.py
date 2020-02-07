#﻿swex 1959 두 개의 숫자열

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
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N >= M:
        L, S = A, B
        Llen,Slen = N,M
    else:
        L, S = B, A
        Llen, Slen = M, N

    maxMulSum = -1
    for i in range(Llen - Slen + 1):
        mulSum = 0
        for j in range(i,i+Slen):
            mulSum += S[j-i] * L[j]
        maxMulSum = max(maxMulSum, mulSum)

    print('#%d'%test_case,maxMulSum)


