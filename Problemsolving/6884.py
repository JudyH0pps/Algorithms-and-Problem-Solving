import sys
sys.stdin = open('input.txt')

primeNumbers = [1] * 50000001
primeNumbers[0] = 0
primeNumbers[1] = 0

for i in range(2, 50000001):
    if primeNumbers[i] == 0:
        continue
    for j in range(i + i, 50000001, i):
        primeNumbers[j] = 0

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    N = nums[0]
    nums = nums[1:]
    minL = N + 1
    s, e = -1, -1
    for i in range(N):
        S = nums[i]
        for j in range(i + 1, min(N, i + minL - 1)):
            S += nums[j]
            if primeNumbers[S]:
                if minL > j - i + 1:
                    minL = j - i + 1
                    s = i
                    e = j
                break

    if s == -1:
        print('This sequence is anti-primed.')
    else:
        print('Shortest primed subsequence is length',
              str(minL) + ':', *nums[s: e + 1])
