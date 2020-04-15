nums = [55, 7, 78, 12, 42]
print(nums)

for i in range(len(nums) - 1):
    for j in range(i, len(nums) - 1 - i):
        if nums[j + 1] < nums[j]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]
    print(nums)
