import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))

if N == 1 or N == 2 and nums[0] != nums[1]:
    print('A')
elif nums[0] == nums[1]:
    x = nums[0]
    for n in nums:
        if x != n:
            print('B')
            break
    else:
        print(nums[0])
else:
    if (nums[2] - nums[1]) % (nums[1] - nums[0]):
        print('B')
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        b = nums[1] - nums[0] * a
        for i in range(1, N - 1):
            if nums[i] * a + b != nums[i + 1]:
                print('B')
                break
        else:
            print(nums[-1] * a + b)
