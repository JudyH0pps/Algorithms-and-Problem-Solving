# ﻿swex 4008 숫자 만들기

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

def DFS(score, last):
    last += 1
    if N == last:
        global maxScore, minScore
        maxScore = max(maxScore, score)
        minScore = min(minScore, score)
        return
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0:
                nscore = score + nums[last]
            elif i == 1:
                nscore = score - nums[last]
            elif i == 2:
                nscore = score * nums[last]
            else:
                nscore = int(score / nums[last])
            path.append(nscore)
            DFS(nscore, last)
            op[i] += 1
            path.pop()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    maxScore = float('-inf')
    minScore = float('inf')
    path = []
    DFS(nums[0], 0)
    print('#%d' % test_case, maxScore - minScore)
