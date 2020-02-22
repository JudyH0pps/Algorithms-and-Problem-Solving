#﻿10570 Favorite Number

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

T = int(input())
for _ in range(T):
    V = int(input())
    nums = {}
    for _ in range(V):
        i = int(input())
        nums[i] = nums.get(i,0) + 1
    print(sorted(nums.items(),key = lambda x : (-x[1],x[0]))[0][0])