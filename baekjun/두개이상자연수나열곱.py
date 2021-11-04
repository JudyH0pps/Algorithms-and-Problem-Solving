import sys, heapq, math

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

up_ptr = 2
nums = []
heapq.heappush(nums, (2, 2, 1))
last = -1
cnt = 0
while True:
    num, idx, left = heapq.heappop(nums)
    if last != num:
        last = num
        # print(num, end=' ')
        cnt += 1
    if cnt == N:
        break
    # print(num, idx, left)
    if idx == up_ptr:
        up_ptr += 1
        heapq.heappush(nums, (math.factorial(up_ptr), up_ptr, 1))

    next_num = num // left * (left + idx)
    heapq.heappush(nums, (next_num, idx, left + 1))

print(last)
