import sys
sys.stdin = open('input.txt', 'r')

primeNumbers = [1] * 100000001
primeNumbers[0] = 0
primeNumbers[1] = 0

for i in range(2, len(primeNumbers)):
    if primeNumbers[i] == 0:
        continue
    for j in range(i + i, len(primeNumbers), i):
        primeNumbers[j] = 0

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    L = nums[0]
    nums = nums[1:]
    minPrimes = [0] * 10001
    for i in range(len(nums) - 1):
        primeSum = nums[i]
        primes = [nums[i]]
        for j in range(i + 1, len(nums)):
            primeSum += nums[j]
            primes.append(nums[j])
            if primeNumbers[primeSum]:
                if len(minPrimes) > len(primes) >= 2:
                    minPrimes = primes
                break
    if len(minPrimes) == 10001:
        print('This sequence is anti-primed.')
    else:
        print('Shortest primed subsequence is length',
              len(minPrimes), ':', end=' ')
        print(*minPrimes)
