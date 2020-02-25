# ﻿1644 소수의 연속합

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

def findPrime(N):
    np = [0] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if not np[i]:
            for j in range(i ** 2, N + 1, i):
                np[j] = 1
    for i in range(2,N+1):
        if not np[i]:
            primes.append(i)


N = int(input())
primes = []
findPrime(N)
cumulSum = [0] * (len(primes)+1)
for i in range(1,len(primes)+1):
    cumulSum[i] = cumulSum[i-1] + primes[i-1]
# print(cumulSum)

count = 0
for left in range(0,len(cumulSum) - 1):
    for dist in range(1,len(cumulSum) - left):
        x = cumulSum[left+dist] - cumulSum[left]
        if x >= N:
            if x == N:
                count += 1
            break
print(count)

