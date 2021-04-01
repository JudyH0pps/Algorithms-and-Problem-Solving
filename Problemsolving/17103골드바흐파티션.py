import sys
sys.stdin = open('input.txt')


nums = list(range(1000001))
nums[0] = nums[1] = 0

for i in range(2, 1000001):
    if nums[i] == 0:
        continue
    for j in range(i * 2, 1000001, i):
        if nums[j] == 0:
            continue
        nums[j] = 0

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N // 2 + 1):
        if nums[i] and nums[N - i]:
            cnt += 1
    print(cnt)
