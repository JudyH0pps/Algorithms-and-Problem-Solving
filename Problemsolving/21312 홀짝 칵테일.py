import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

mulOdds = 1
mul = 1
oddOK = False

for num in nums:
    if num % 2:
        mulOdds *= num
        oddOK = True
    mul *= num

if oddOK:
    print(mulOdds)
else:
    print(mul)
