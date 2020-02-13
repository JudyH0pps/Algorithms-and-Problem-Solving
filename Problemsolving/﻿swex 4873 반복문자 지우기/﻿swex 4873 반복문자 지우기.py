#﻿swex 4873 반복문자 지우기

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
for test_case in range(1,T+1):
    s = input()
    left = -1
    stack = ['']
    for c in s:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print('#%d'%test_case,len(stack)-1)