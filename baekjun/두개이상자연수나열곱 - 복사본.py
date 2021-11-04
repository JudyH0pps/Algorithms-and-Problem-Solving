import sys, heapq, math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

nums = set()
nums.add(2)

for i in range(2, 10 ** 7 + 1):
    j = i
    n = j
    while True:
        n = n * (j + 1)
        if n > 10 ** 14:
            break
        nums.add(n)
        j += 1

nums = sorted(list(nums))
print(nums[N-1])
print(len(nums))



