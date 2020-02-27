# ﻿swex 1486 장훈의의 높은 선반

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

def pick(last, score):
    # print(score)
    for i in range(last + 1, N):
        if score + nums[i] + cumul[i + 1] < B:
            continue
        if score + nums[i] >= B:
            global mindiff
            mindiff = min(mindiff, score + nums[i] - B)
            continue
        pick(i, score + nums[i])


T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))
    cumul = [0] * (N + 1)
    cumul[-2] = nums[-1]
    for i in range(N - 2, -1, -1):
        cumul[i] += cumul[i + 1] + nums[i]
    # print(nums)
    # print(cumul)
    mindiff = float('inf')
    pick(-1, 0)
    print('#%d' % test_case, mindiff)
